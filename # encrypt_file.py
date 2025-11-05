# encrypt_file.py

import sys
import subprocess
import os

try:
    from cryptography.fernet import Fernet
except ImportError:
    print("Installing required module: cryptography...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "cryptography"])
    from cryptography.fernet import Fernet  # import again after install

if len(sys.argv) < 2:
    print("Usage: python encrypt_file.py <filename>")
    sys.exit(1)

filename = sys.argv[1]
if not os.path.exists(filename):
    print(f"Error: File '{filename}' not found.")
    sys.exit(1)

key = Fernet.generate_key()
cipher = Fernet(key)
with open(filename, "rb") as file:
    data = file.read()
    encrypted = cipher.encrypt(data)

enc_filename = filename + ".enc"
with open(enc_filename, "wb") as file:
    file.write(encrypted)

print(f"\n File encrypted successfully!")
print(f"Encrypted file saved as: {enc_filename}")
print(f"Save this key to decrypt later:\n{key.decode()}")
