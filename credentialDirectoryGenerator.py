import csv
import os
import json
from changeFilePaths import filePathSeparator
from databaseConnection import create_connection, create_credentials
from passwordGenerator import generate_passwords


def generate_credential_dir():
    fPathLoopStop = False

    while not fPathLoopStop:
        user_filePath = input("Please enter the full path with filename that contains your CSV file of usernames and websites: ")
        if os.path.exists(user_filePath) and os.path.isfile(user_filePath) and user_filePath.endswith(".csv"):
            fPathLoopStop = True
        else:
            print("Oops, you didn't enter a valid file path/file name. Please try again!")

    # open/read username and website list
    userFile = open(user_filePath, 'r')
    userFileReader = csv.reader(userFile)
    userFileData = list(userFileReader)
    userFile.close()
    # print(userFileData)

    # open/read/store JSON config file in variable
    configFile = open('pmConfig.json', 'r')
    json_filePath = json.load(configFile)
    configFile.close()
    outputFile_path = json_filePath["output_file_path"]

    # open password list binary file
    try:
        password_list = open(outputFile_path + f"{filePathSeparator}password_list.bin", "rb")
    except:
        print("\nIt looks like you haven't generated any passwords yet! Please select Option 1 for the password generator.")
        quit()

    # password_list = open(outputFile_path + f"{filePathSeparator}password_list.bin", "rb")
    passwordFileData = list(password_list)

    database = r"pythonsqlite.db"
    conn = create_connection(database)
    count = 0
    for user_row in userFileData:
        user_row.append(passwordFileData[count])
        credential = user_row[0], user_row[1], user_row[2]
        create_credentials(conn, credential)
        count += 1
        # print(user_row)


def view_cred_dictionary():
    print("")
