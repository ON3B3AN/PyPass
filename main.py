import passwordGenerator as passGen
from termcolor import colored
import encryptDecrypt as crypt
import changeFilePaths as fPath
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
    print(colored("Main Menu", "grey", attrs=['bold', 'underline']))
    print("""
    1. Generate Passwords
    2. View Passwords
    3. Create Credential Dictionary
    4. Modify path configurations
    5. Exit
    """)
    option = input("Enter an option: ")
    if option == "1":
        passGen.generate_passwords()
    elif option == "2":
        crypt.decrypt_passwords()
    elif option == "3":
        pass
    elif option == "4":
        print(colored("\nFile Path Configuration Menu", "grey", attrs=['bold', 'underline']))
        print("""
    1. Modify the removable disk path
    2. Modify output file path
        """)
        option = input("Enter an option: ")
        if option == "1":
            fPath.changeRmMediaPath()
        elif option == "2":
            fPath.changePwdOutputFilePath()
    elif option == "5":
        sys.exit()


while __name__ == "__main__":
    main_menu()
