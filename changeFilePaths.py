import platform
from pathlib import Path
import json

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
    print("Changing Removable Media File Path")
    rmFileLoopStop = True
    while rmFileLoopStop:
        rm_media_path = Path(input("Enter drive letter for removable media: ") + rmDiskSuffix)
        print("The path for removable media is:", rm_media_path)
        if rm_media_path.exists():
            filePath["rm_media_path"] = str(rm_media_path)
            configFile = open('pmConfig.json', 'w')
            json.dump(filePath, configFile)
            configFile.close()
            rmFileLoopStop = False
        else:
            print("Oops, that's an invalid file path, or it does not exist! Make sure your removable media is plugged in. Please try again!")


def checkConfigPaths():
    if filePath["rm_media_path"] == "":
        changeRmMediaPath()
