from cryptography.fernet import Fernet

rm_media_path = input("Enter drive letter for removable media: ").upper() + ":\\"


def generate_key():
    """
    Generates a key and save it into a file
    """
    print("Generating secret key...")
    key = Fernet.generate_key()
    with open(rm_media_path + "secret.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    """
    Load the previously generated key
    """
    return open(rm_media_path + "secret.key", "rb").read()


def encrypt_password(password, output_file):
    """
    Encrypts a password
    """
    key = load_key()
    encoded_password = password.encode()
    f = Fernet(key)
    encrypted_password = f.encrypt(encoded_password)
    output_file.write(encrypted_password)
    output_file.write("\n".encode())


def decrypt_passwords():
    """
    Decrypts encrypted passwords
    """
    key = load_key()
    f = Fernet(key)
    input_file = open('.\\password_list.bin', "rb").read()
    print("")
    for password in input_file.splitlines():
        decrypted_password = f.decrypt(bytes(password))
        print(decrypted_password.decode())
