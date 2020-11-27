import csv
import os
import json
from databaseConnection import create_connection, create_credentials, clear_password_db
from passwordGenerator import configure_passwords
from termcolor import colored


def generate_credential_dir(update):
    if not update:
        print("""
***********************************************************************************
                               Instructions:
  • Create and save a csv file that contains usernames and websites in that order
***********************************************************************************""")
        # clear credential table is not updating
        terminate = clear_password_db()
    elif update:
        print(colored("\nWarning! Csv file containing usernames and websites must only contain NEW entries!", "yellow", attrs=["bold"]))
        terminate = update
    else:
        terminate = update

    if not terminate:
        return

    fPathLoopStop = False
    while not fPathLoopStop:
        user_filePath = input("Please enter the full path with filename that contains your CSV file of usernames and websites: ")
        if os.path.exists(user_filePath) and os.path.isfile(user_filePath) and user_filePath.endswith(".csv"):
            fPathLoopStop = True
        else:
            print(colored("Oops, you didn't enter a valid file path/file name. Please try again!", "red", attrs=['bold']))

    # open/read username and website list
    userFile = open(user_filePath, 'r')
    userFileReader = csv.reader(userFile)
    userFileData = list(userFileReader)

    # clear empty sets in a list
    username_list = list(filter(None, userFileData))
    num_usernames = len(username_list)
    configure_passwords(num_usernames, update)
    userFile.close()

    # open/read/store JSON config file in variable
    configFile = open('pmConfig.json', 'r')
    json_filePath = json.load(configFile)
    configFile.close()

    # check if password list has been successfully generated
    try:
        password_list = open("password_list.bin", "rb")
        passwordFileData = list(password_list)
        password_list.close()
    except:
        print(colored("\nIt looks like you haven't generated any passwords yet! Please select Option 1 for the password generator.", "red", attrs=['bold']))
        quit()

    database = r"pythonsqlite.db"
    conn = create_connection(database)
    count = 0
    for user_row in username_list:
        user_row.append(passwordFileData[count])
        credential = user_row[0], user_row[1], user_row[2]
        create_credentials(conn, credential)
        count += 1

    os.remove("password_list.bin")
