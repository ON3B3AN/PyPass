import platform
from pathlib import Path
import json

configFile = open('pmConfig.json','r')
filePath = json.load(configFile)
configFile.close()


print("You are running", platform.system())

if platform.system() == "Windows":
    filePathSeparator = "\\"
    rmDiskSuffix = ":\\"
else:
    filePathSeparator = "/"
    rmDiskSuffix = "/"

print("filePathSuffix:", filePathSeparator)
print("rmDiskSuffix:", rmDiskSuffix)


def changeRmMediaPath():
    print("[changeFilePaths.py] Changing Removable Media File Path")
    rmFileLoopStop = True
    while rmFileLoopStop:
        rm_media_path = Path(input("Enter drive letter for removable media: ") + rmDiskSuffix)
        print("The path for removable media is:", rm_media_path)
        if rm_media_path.exists():
            # cfg.filePaths["output_file_path"] = str(rm_media_path)
            filePath["rm_media_path"] = str(rm_media_path)
            configFile = open('pmConfig.json', 'w')
            json.dump(filePath, configFile)
            configFile.close()
            rmFileLoopStop = False
        else:
            print("Oops, that's not a valid file path. Please try again!")


def changePwdOutputFilePath():
    print("[changeFilePaths.py] Changing Password output File Path")
    outputFileLoopStop = True
    while outputFileLoopStop:
        output_file_path = Path(input("Enter file path for output file pwd list: ") + filePathSeparator)
        print("The output path for the passwords list is:", output_file_path)
        if output_file_path.exists():
            # Modify config file (pmConfig.py)
            filePath["output_file_path"] = str(output_file_path)
            configFile = open('pmConfig.json', 'w')
            json.dump(filePath, configFile)
            configFile.close()
            outputFileLoopStop = False
        else:
            print("Oops, that's not a valid file path. Please try again!")
