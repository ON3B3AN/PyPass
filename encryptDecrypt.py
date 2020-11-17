import csv
from cryptography.fernet import Fernet
from pathlib import Path

cwd = Path.cwd()


def generate_key():
    """
    Generates a key and save it into a file
    """
    print("Generating secret.key...")
    print("It is highly recommended to store the secret.key on removable media (USB)")
    key_path = input("Enter the path to store the secret.key (I.E.; D:\\\): ")
    key = Fernet.generate_key()
    with open(f"{key_path}secret.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    """
    Load the previously generated key
    """
    print("Loading secret.key...")
    key_path = input("Enter the path to the secret.key: ")
    return open(f"{key_path}secret.key", "rb").read()


def encrypt_password(password):
    """
    Encrypts a message
    """
    key = load_key()
    encoded_password = password.encode()
    f = Fernet(key)
    with open("../passwordManager/passwordManager/password_list.csv", "w", newline="") as output_file:
        output_writer = csv.writer(output_file)
        encrypted_password = f.encrypt(encoded_password)
        output_writer.writerow([encrypted_password])


def decrypt_message():
    """
    Decrypts an encrypted message
    """
    key = load_key()
    f = Fernet(key)
    with open('../passwordManager/passwordManager/password_list.csv') as input_file:
        input_reader = csv.reader(input_file)
        for row in input_reader:
            decrypted_password = f.decrypt(row)
            print(decrypted_password.decode())
