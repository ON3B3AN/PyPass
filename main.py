import passwordGenerator as passGen
from termcolor import colored
import encryptDecrypt as crypt
import changeFilePaths as fPath
import credentialDirectoryGenerator as credDir
import sys


def main_menu():
    print(colored("""
██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗ 
██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗
██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║
██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║
██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ 

███╗   ███╗ █████╗ ███╗   ██╗ █████╗  ██████╗ ███████╗██████╗      
████╗ ████║██╔══██╗████╗  ██║██╔══██╗██╔════╝ ██╔════╝██╔══██╗     
██╔████╔██║███████║██╔██╗ ██║███████║██║  ███╗█████╗  ██████╔╝     
██║╚██╔╝██║██╔══██║██║╚██╗██║██╔══██║██║   ██║██╔══╝  ██╔══██╗     
██║ ╚═╝ ██║██║  ██║██║ ╚████║██║  ██║╚██████╔╝███████╗██║  ██║     
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝     
    """, "yellow", attrs=['bold']))
    fPath.checkConfigPaths()
    print(colored("Main Menu", "grey", attrs=['bold', 'underline']))
    print("""
    1. Generate Passwords
    2. View Passwords
    3. Generate Credential Dictionary
    4. View Credential Dictionary
    5. Modify Path Configurations
    6. Exit
    """)
    option = input("Enter an option: ")
    if option == "1":
        passGen.generate_passwords()
    elif option == "2":
        crypt.decrypt_passwords()
    elif option == "3":
        credDir.generate_credential_dir()
    elif option == "4":
        pass
    elif option == "5":
        print(colored("\nPath Configuration Menu", "grey", attrs=['bold', 'underline']))
        print("""
    1. Modify Removable Media Path
    2. Modify Output File Path
        """)
        option = input("Enter an option: ")
        if option == "1":
            fPath.changeRmMediaPath()
        elif option == "2":
            fPath.changePwdOutputFilePath()
    elif option == "6":
        sys.exit()


while __name__ == "__main__":
    main_menu()
