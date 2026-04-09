# 🛡️ GuardianVault -  Secure File Management System

**GuardianVault** is a high-security file management dashboard that implements industrial-grade encryption to protect sensitive data. Built with Python and Streamlit, it provides a seamless interface for secure file storage, role-based access, and transparent auditing.

### 🌐 [**View Live Demo**](https://mini-secure-file-system-evmko9cwkbwwpf9ru3cnhq.streamlit.app/)

```
Default username - admin
Default Password - admin123
```
<img width="1918" height="964" alt="Screenshot 2026-04-09 143030" src="https://github.com/user-attachments/assets/902a54d5-ad2b-4c94-9c0d-9c7f751cba68" />
<img width="1900" height="945" alt="Screenshot 2026-04-09 143049" src="https://github.com/user-attachments/assets/dec918c9-4544-4d66-8a11-6c3733034ca4" />
<img width="1908" height="973" alt="Screenshot 2026-04-09 143119" src="https://github.com/user-attachments/assets/451e656c-7eec-4d64-9cee-29acc5a903db" />
<img width="1916" height="958" alt="Screenshot 2026-04-09 143135" src="https://github.com/user-attachments/assets/663db7ff-03f5-490f-8c4e-242b412dcf97" />
<img width="1918" height="959" alt="Screenshot 2026-04-09 143147" src="https://github.com/user-attachments/assets/5055d6fa-79da-4aad-8015-5d199539068d" />
<img width="1918" height="960" alt="Screenshot 2026-04-09 143209" src="https://github.com/user-attachments/assets/469d53a9-36b0-47f6-a272-718e9ceec8d9" />
<img width="1919" height="966" alt="Screenshot 2026-04-09 143219" src="https://github.com/user-attachments/assets/7edcf91f-ff25-4872-a062-78c08515053d" />

---

## 🚀 Key Features

* **AES-128 Encryption:** Files are encrypted at the binary level using the Fernet symmetric encryption standard.
* **Persistent Key Logic:** Implements a localized key-management strategy to ensure data integrity across sessions.
* **Role-Based Access Control (RBAC):** * **User:** Securely upload, decrypt, and manage personal vault files.
    * **Admin:** Access the global audit trail and monitor system-wide encrypted storage.
* **Live Audit Logging:** Real-time logging of user activities (logins, uploads, deletions) for accountability.
* **Binary File Support:** Specialized handling for PDFs, Images, and Documents via secure download-on-decryption.

## 🛠️ Technical Architecture

* **Security Layer:** `Cryptography` library (Fernet), `Hashlib` (SHA-256 password hashing).
* **Frontend:** `Streamlit` (Web Interface).
* **Backend:** Python File I/O & JSON-based mock database.
* **Deployment:** Streamlit Cloud with GitHub CI/CD integration.

## 📂 Repository Structure

```text
├── secure_app.py      # Core Application logic
├── secret.key         # Master Encryption Key (Auto-generated)
├── users.json         # Encrypted User Database
├── audit_log.txt      # System-wide Audit Trail
├── vault/             # Encrypted Storage Directory
├── .gitignore         # Security filter for sensitive files
└── requirements.txt   # Python dependency list
````

## ⚙️ Quick Start

1.  **Clone the Repo:**
    ```bash
    git clone git@github.com:anushka-cseatmnc/Mini-Secure-File-System.git
    cd Mini-Secure-File-System
    ```
2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Launch the Vault:**
    ```bash
    streamlit run secure_app.py
    ```

## 🛡️ Security Posture

### Data at Rest

Files are stored as encrypted blobs in the `vault/` directory. Without the unique `secret.key`, the files are mathematically irrecoverable, providing strong protection against unauthorized physical access to the server storage.

### Identity Management

Passwords undergo a **SHA-256 one-way hash** before storage. This ensures that even in the event of a database leak, original user passwords remain protected as the hash cannot be reversed to reveal the plain-text credentials.

-----

