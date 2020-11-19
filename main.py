import passwordGenerator as passGen
from termcolor import colored
import encryptDecrypt as crypt
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
    4. Exit
    """)
    option = input("Enter an option: ")
    if option == "1":
        # passGen.generate_passwords()
        passGen.generate_passwords()
    elif option == "2":
        # crypt.decrypt_passwords()
        crypt.decrypt_passwords()
    elif option == "3":
        pass
    elif option == "4":
        sys.exit()


while __name__ == "__main__":
    main_menu()
