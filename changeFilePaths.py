import platform
from pathlib import Path
import json
import os
from termcolor import colored

configFile = open('pmConfig.json', 'r')
filePath = json.load(configFile)
configFile.close()

if platform.system() == "Windows":
    filePathSeparator = "\\"
    rmDiskSuffix = ":\\"
else:
    filePathSeparator = "/"
    rmDiskSuffix = "/"


def changeRmMediaPath():
    rmFileLoopStop = True
    while rmFileLoopStop:
        rm_media_path = input("Enter drive letter or path for removable media: ") + rmDiskSuffix
        if Path(rm_media_path).exists():
            print("The path for removable media is:", rm_media_path)
            filePath["rm_media_path"] = str(rm_media_path)
            configFile = open('pmConfig.json', 'w')
            json.dump(filePath, configFile)
            configFile.close()
            rmFileLoopStop = False
            if not os.listdir(Path(rm_media_path)):
                mount_rm_media(rm_media_path)
        else:
            print(colored("Oops, that's an invalid file path, or it does not exist! Make sure your removable media is plugged in. Please try again!", "red", attrs=['bold']))


def mount_rm_media(rm_media_path):
    if Path(rm_media_path).exists():
        # Assume if removable drive is empty, then the drive isn't mounted
        if not os.listdir(Path(rm_media_path)):
            option_1 = input("Would you like to mount this removable drive? (y/n): ")
            if option_1 == "Y" or option_1 == "y":
                drive_letter = rm_media_path[-2]
                try:
                    # The following command only works for Linux and WSL
                    os.system(f"sudo mount -t drvfs {drive_letter}: /mnt/{drive_letter}")
                    print(colored(f"{rm_media_path} mounted successfully!\n", "green", attrs=["bold"]))
                except:
                    print("Error, couldn't mount removable drive")
    else:
        changeRmMediaPath()


def checkConfigPaths():
    if filePath["rm_media_path"] == "":
        changeRmMediaPath()
    elif not os.listdir(Path(filePath["rm_media_path"])):
        mount_rm_media(filePath["rm_media_path"])


def get_rm_media_path():
    rm_media_output_file = filePath["rm_media_path"] + filePathSeparator + "secret.key"
    return rm_media_output_file
