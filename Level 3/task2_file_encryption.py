import os
from cryptography.fernet import Fernet

def generate_key():
    if not os.path.exists("secret.key"):
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
        print("🔑 New encryption key generated and saved to 'secret.key'")

def load_key():
    return open("secret.key", "rb").read()

def encrypt_file(filename):
    try:
        key = load_key()
        f = Fernet(key)
        with open(filename, "rb") as file:
            file_data = file.read()
        encrypted_data = f.encrypt(file_data)
        
        output_filename = filename + ".enc"
        with open(output_filename, "wb") as file:
            file.write(encrypted_data)
        print(f"✅ File encrypted successfully! Saved as: {output_filename}")
    except FileNotFoundError:
        print(f"❌ Error: File '{filename}' not found.")
    except Exception as e:
        print(f"❌ Error during encryption: {e}")

def decrypt_file(filename):
    try:
        key = load_key()
        f = Fernet(key)
        with open(filename, "rb") as file:
            encrypted_data = file.read()
        decrypted_data = f.decrypt(encrypted_data)
        
        output_filename = filename.replace(".enc", "_decrypted.txt")
        with open(output_filename, "wb") as file:
            file.write(decrypted_data)
        print(f"🔓 File decrypted successfully! Saved as: {output_filename}")
    except FileNotFoundError:
        print(f"❌ Error: File '{filename}' not found.")
    except Exception as e:
        print(f"❌ Decryption failed! Invalid key or corrupted file.")

def main():
    generate_key()
    while True:
        print("\n===== FILE ENCRYPTION / DECRYPTION =====")
        print("1. Encrypt a File\n2. Decrypt a File\n3. Exit")
        choice = input("Enter choice (1-3): ").strip()

        if choice == "1":
            fname = input("Enter filename to encrypt (e.g., myfile.txt): ").strip()
            encrypt_file(fname)
        elif choice == "2":
            fname = input("Enter filename to decrypt (e.g., myfile.txt.enc): ").strip()
            decrypt_file(fname)
        elif choice == "3":
            print("👋 Exiting File Encryption Tool.")
            break
        else:
            print("❌ Invalid choice, try again.")

if __name__ == "__main__":
    main()