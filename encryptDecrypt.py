# from passwordGenerator import *
# import passwordGenerator as genPass
# from passwordGenerator import *
from cryptography.fernet import Fernet
from pathlib import Path
import platform

print("You are running", platform.system())

if platform.system() == "Windows":
    filePathSeparator = "\\"
    rmDiskSuffix = ":\\"
else:
    filePathSeparator = "/"
    rmDiskSuffix = "/"

print("filePathSuffix:", filePathSeparator)
print("rmDiskSuffix:", rmDiskSuffix)

# Path differences for Windows vs. Mac and Linux -- keep for future reference if needed
# rm_media_path = input("Enter drive letter or path for removable media: ").upper() + ":\\"
# rm_media_path = input("Enter drive letter or path for removable media: ") + "/"

rmFileLoopStop = True
while rmFileLoopStop:
    rm_media_path = Path(input("Enter drive letter for removable media: ") + rmDiskSuffix)
    print("The path for removable media is:", rm_media_path)
    if rm_media_path.exists():
        rmFileLoopStop = False
    else:
        print("Oops, that's not a valid file path. Please try again!")


outputFileLoopStop = True
while outputFileLoopStop:
    output_file_path = Path(input("Enter file path for output file pwd list: ") + filePathSeparator)
    print("The output path for the passwords list is:", output_file_path)
    if output_file_path.exists():
        outputFileLoopStop = False
    else:
        print("Oops, that's not a valid file path. Please try again!")


def get_output_file_path():
    return output_file_path


def generate_key():
    """
    Generates a key and save it into a file
    """
    print("Generating secret key...")
    key = Fernet.generate_key()
    # old open syntax: open(rm_media_path + "secret.key", "wb") - changed + to / to append key to POSIX path: https://stackoverflow.com/questions/48190959/how-do-i-append-a-string-to-a-path-in-python
    with open(rm_media_path / "secret.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    """
    Load the previously generated key
    """
    return open(rm_media_path / "secret.key", "rb").read()


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
    # input_file = open(f'{output_file_path}\\password_list.bin', "rb").read()
    input_file = open(f'{output_file_path}{filePathSeparator}password_list.bin', "rb").read()
    print("")
    for password in input_file.splitlines():
        decrypted_password = f.decrypt(bytes(password))
        print(decrypted_password.decode())
