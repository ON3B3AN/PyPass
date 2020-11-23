from pathlib import Path
import csv
import os


def generate_credential_dir():
    fPathLoopStop = False

    while not fPathLoopStop:
        filePath = input("Please enter the full path with filename that contains your CSV file of usernames and websites: ")
        if os.path.exists(filePath) and os.path.isfile(filePath):
            fPathLoopStop = True
        else:
            print("Oops, you didn't enter a valid file path/file name. Please try again!")

    userFile = open(filePath,'r')
    userFileReader = csv.reader(userFile)
    userFileData = list(userFileReader)
    userFile.close()

    print(userFileData)

    userPwFile = open(filePath,'w',newline='')
    userPwFileWriter = csv.writer(userPwFile)

    for row in userFileData:
        print("list row:", row)
        row.append("password")
        userPwFileWriter.writerow(row)

    userPwFile.close()
