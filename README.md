Here is the complete **README.md** code formatted in a raw block so you can copy and paste it directly into your file.

````markdown
# 🛡️ GuardianVault: Secure File Management System

**GuardianVault** is a high-security file management dashboard that implements industrial-grade encryption to protect sensitive data. Built with Python and Streamlit, it provides a seamless interface for secure file storage, role-based access, and transparent auditing.

### 🌐 [**View Live Demo**](https://mini-secure-file-system-evmko9cwkbwwpf9ru3cnhq.streamlit.app/)

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

## 👤 Author

**Anushka**

  * CS Student | Security Enthusiast
  * [GitHub Profile](https://www.google.com/search?q=https://github.com/anushka-cseatmnc)

<!-- end list -->

```
```
