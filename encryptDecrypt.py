# Portions of this file referenced from: https://devqa.io/encrypt-decrypt-data-python/

import xlwt
from xlwt import Workbook
from cryptography.fernet import Fernet
from pathlib import Path
import platform
import json
import os
from termcolor import colored

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
    print(colored("Username: ", "white", attrs=["bold"]) + colored(str(password[1]), "grey", attrs=["bold"]) +
          colored("  Website: ", "white", attrs=["bold"]) +
          colored(str(password[2]), "blue", attrs=["bold", "underline"]) +
          colored("  Password: ", "white", attrs=["bold"]) + colored("{", "green", attrs=["bold"]) +
          colored(decrypted_password.decode(), "white", attrs=["concealed"]) + colored("}", "green", attrs=["bold"]))


def backup_decrypt_passwords(credentials):
    """
    Decrypts encrypted passwords and makes a backup file
    """
    key = load_key()
    f = Fernet(key)

    # Workbook is created
    wb = Workbook()

    # add_sheet is used to create sheet
    sheet1 = wb.add_sheet('Sheet 1')

    # Specifying style
    style = xlwt.easyxf('font: bold 1')

    # headers
    sheet1.write(0, 0, 'Username', style)
    sheet1.write(0, 1, 'Website', style)
    sheet1.write(0, 2, 'Password', style)

    row_num = 1
    for index in credentials:
        decrypted_password = f.decrypt(bytes(index[3]))
        sheet1.write(row_num, 0, index[1])
        sheet1.write(row_num, 1, index[2])
        sheet1.write(row_num, 2, decrypted_password.decode())
        row_num += 1

    fPathLoopStop = False
    while not fPathLoopStop:
        backup_path = input("Enter fully qualified path to store backup Credential Dictionary: ")
        if os.path.exists(backup_path):
            wb.save(f'{backup_path}{filePathSeparator}PyPass_Credential_Dictionary.xls')
            print("\n" + colored("Successfully backed up Credential Dictionary!", "green", attrs=["bold"]) +
                  f"\nBackup located at: {backup_path}{filePathSeparator}PyPass_Credential_Dictionary.xls")
            fPathLoopStop = True
        else:
            print(colored("Oops, you didn't enter a valid file path. Please try again!", "red", attrs=['bold']))
