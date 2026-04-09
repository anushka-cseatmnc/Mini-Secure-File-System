import streamlit as st
import pandas as pd
import os
import json
from datetime import datetime
from cryptography.fernet import Fernet
import hashlib

# --- DIRECTORY & FILE SETUP ---
DB_FILE = "users.json"
STORAGE_DIR = "vault"
LOG_FILE = "audit_log.txt"
KEY_FILE = "secret.key"

if not os.path.exists(STORAGE_DIR): os.makedirs(STORAGE_DIR)

# --- KEY MANAGEMENT ---
def load_or_create_key():
    if os.path.exists(KEY_FILE):
        return open(KEY_FILE, "rb").read()
    else:
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)
        return key

cipher = Fernet(load_or_create_key())

# --- MOCK DATABASE ---
def load_users():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, 'r') as f: return json.load(f)
    return {"admin": {"pw": hashlib.sha256("admin123".encode()).hexdigest(), "role": "admin"}}

def log_event(user, action):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {user}: {action}\n")

# --- UI CONFIG ---
st.set_page_config(page_title="GuardianVault", page_icon="🛡️", layout="wide")

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# --- LOGIN PAGE ---
if not st.session_state.logged_in:
    _, col, _ = st.columns([1, 1.5, 1])
    with col:
        st.title("🛡️ GuardianVault")
        with st.container(border=True):
            user = st.text_input("Username")
            pw = st.text_input("Password", type="password")
            if st.button("Access Vault"):
                users = load_users()
                hashed_pw = hashlib.sha256(pw.encode()).hexdigest()
                if user in users and users[user]['pw'] == hashed_pw:
                    st.session_state.logged_in = True
                    st.session_state.user = user
                    st.session_state.role = users[user]['role']
                    log_event(user, "Logged In")
                    st.rerun()
                else:
                    st.error("Invalid Credentials")
else:
    # --- NAVIGATION ---
    with st.sidebar:
        st.header("GuardianVault")
        st.write(f"👤 **{st.session_state.user}**")
        st.divider()
        menu = ["📂 My Vault", "📤 Secure Upload", "🛠️ Admin Console"]
        choice = st.radio("Navigation", menu if st.session_state.role == "admin" else menu[:2])
        if st.sidebar.button("Logout"):
            st.session_state.logged_in = False
            st.rerun()

    # --- MY VAULT (WITH DELETE) ---
    if choice == "📂 My Vault":
        st.header("Your Secure Files")
        files = [f for f in os.listdir(STORAGE_DIR) if f.startswith(st.session_state.user)]
        
        if not files:
            st.info("Vault is empty.")
        else:
            for f_name in files:
                display_name = f_name.replace(f"{st.session_state.user}_", "").replace(".enc", "")
                with st.expander(f"📄 {display_name}"):
                    c1, c2, c3 = st.columns([3, 1, 1])
                    c1.write("AES-128 Encrypted")
                    
                    # DECRYPT BUTTON
                    if c2.button("Decrypt", key=f"dec_{f_name}"):
                        try:
                            with open(os.path.join(STORAGE_DIR, f_name), "rb") as f:
                                decrypted_data = cipher.decrypt(f.read())
                                st.success("Decryption Successful!")
                                st.download_button("💾 Download", decrypted_data, file_name=display_name)
                        except:
                            st.error("Key Mismatch!")

                    # DELETE BUTTON (The new feature)
                    if c3.button("🗑️ Delete", key=f"del_{f_name}"):
                        os.remove(os.path.join(STORAGE_DIR, f_name))
                        log_event(st.session_state.user, f"Deleted: {display_name}")
                        st.warning(f"Deleted {display_name}")
                        st.rerun()

    # --- UPLOAD ---
    elif choice == "📤 Secure Upload":
        st.header("Secure Upload")
        uploaded_file = st.file_uploader("Choose file")
        if uploaded_file and st.button("🔒 Encrypt"):
            content = uploaded_file.read()
            enc_content = cipher.encrypt(content)
            with open(os.path.join(STORAGE_DIR, f"{st.session_state.user}_{uploaded_file.name}.enc"), "wb") as f:
                f.write(enc_content)
            log_event(st.session_state.user, f"Uploaded: {uploaded_file.name}")
            st.success("Encrypted!")

    # --- ADMIN ---
    elif choice == "🛠️ Admin Console":
        st.header("System Logs")
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, "r") as f:
                st.text_area("Audit Trail", f.read(), height=300)