from termcolor import colored
import changeFilePaths as fPath
import credentialDirectoryGenerator as credDir
import databaseConnection as db
import sys
from pathlib import Path


def main_menu():
    print(colored("""
 ███████████             ███████████                           
░░███░░░░░███           ░░███░░░░░███                          
 ░███    ░███ █████ ████ ░███    ░███  ██████    █████   █████ 
 ░██████████ ░░███ ░███  ░██████████  ░░░░░███  ███░░   ███░░  
 ░███░░░░░░   ░███ ░███  ░███░░░░░░    ███████ ░░█████ ░░█████ 
 ░███         ░███ ░███  ░███         ███░░███  ░░░░███ ░░░░███
 █████        ░░███████  █████       ░░████████ ██████  ██████ 
░░░░░          ░░░░░███ ░░░░░         ░░░░░░░░ ░░░░░░  ░░░░░░  
               ███ ░███                                        
              ░░██████                                         
               ░░░░░░                                          
    """, "yellow", attrs=['bold']))
    fPath.checkConfigPaths()
    print(colored("Main Menu", "grey", attrs=['bold', 'underline']))
    print("""
    1. Manage Credential Dictionary
    2. Modify Removable Media Path
    3. Exit
    """)
    option = input("Enter an option: ")
    if option == "1":
        print(colored("\nCredential Dictionary Menu", "grey", attrs=['bold', 'underline']))
        print("""
    1. Add To Existing Credential Dictionary
    2. Create New Credential Dictionary
    3. View Credential Dictionary
    4. Clear Credential Dictionary
            """)
        option = input("Enter an option [press <enter> for main menu]: ")
        if option == "1":
            if Path(fPath.get_rm_media_path()).exists():
                credDir.generate_credential_dir(True)
            else:
                print(colored("No Credential Dictionary was found. Please create one before adding to it.", "red", attrs=["bold"]))
        if option == "2":
            credDir.generate_credential_dir(False)
        if option == "3":
            db.select_all_credentials()
        if option == "4":
            db.clear_password_db()
    elif option == "2":
        fPath.changeRmMediaPath()
    elif option == "3":
        sys.exit()


while __name__ == "__main__":
    main_menu()
