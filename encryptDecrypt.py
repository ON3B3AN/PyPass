from cryptography.fernet import Fernet
from pathlib import Path
import platform
import json

if platform.system() == "Windows":
    filePathSeparator = "\\"
    rmDiskSuffix = ":\\"
else:
    filePathSeparator = "/"
    rmDiskSuffix = "/"


def load_json_config():
    configFile = open('pmConfig.json', 'r')
    filePaths = json.load(configFile)
    configFile.close()
    return filePaths

jsonConfig = load_json_config()
rm_media_path = Path(jsonConfig["rm_media_path"])


def generate_key():
    """
    Generates a key and save it into a file
    """
    print("Generating secret key...")
    key = Fernet.generate_key()
    rm_media_path = load_json_config()["rm_media_path"]
    with open(rm_media_path + filePathSeparator + "secret.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    """
    Load the previously generated key
    """
    rm_media_path = load_json_config()["rm_media_path"]
    return open(rm_media_path + filePathSeparator + "secret.key", "rb").read()


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


def decrypt_passwords(password):
    """
    Decrypts encrypted passwords
    """
    key = load_key()
    f = Fernet(key)

    decrypted_password = f.decrypt(bytes(password[3]))
    print("Username: " + str(password[1]) + " Website: " + str(password[2]) + " Password: " + decrypted_password.decode())
