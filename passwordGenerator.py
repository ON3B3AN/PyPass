import passwordStrengthTest as test
from encryptDecrypt import *
import random


def configure_passwords(num, update):
    if not update:
        generate_key()

    output_file = open("password_list.bin", "wb")
    uppercase_letters = "ABCDEFGHIJKLNMOPQRSTUVWXYZ"
    lowercase_letters = uppercase_letters.lower()
    digits = "0123456789"
    ambiguous_characters = "{}[]()/\\\'\"`~,;:.<> "
    symbols = "@#$%!&*"

    upper, lower, nums = True, True, True

    numLoopStop = False
    while not numLoopStop:
        if not num > 1:
            print(colored("Number of passwords must be more than 1! Please try again...", "red", attrs=['bold']))
        else:
            numLoopStop = True

    lenLoopStop = False
    while not lenLoopStop:
        try:
            length = int(input("Enter your desired password length (min: 8): "))
        except:
            print(colored("You did not enter a valid Integer; please try again!", "red", attrs=['bold']))
            continue

        if length < 8:
            print(colored("Length of password is", length, ", which is less than 8! Please try again...", "red", attrs=['bold']))
        else:
            lenLoopStop = True

    def add_symbols(answer):
        if answer.upper() == "Y" or answer.lower() == "y":
            syms = True
        elif answer.upper() == "N" or answer.lower() == "n":
            syms = False
        else:
            print(colored("Input not recognized", "red", attrs=['bold']))
            syms = add_symbols(input("Use symbols? (y/n): "))
        return syms

    def add_ambiguous_characters(answer):
        if answer.upper() == "Y" or answer.lower() == "y":
            chars = True
        elif answer.upper() == "N" or answer.lower() == "n":
            chars = False
        else:
            print(colored("Input not recognized", "red", attrs=['bold']))
            chars = add_ambiguous_characters(input("Use ambiguous characters? (y/n): "))
        return chars

    def generate_password(syms, chars, hit=0, miss=0):
        password = ""
        if upper:
            password += uppercase_letters
        if lower:
            password += lowercase_letters
        if nums:
            password += digits
        if syms:
            password += symbols
        if chars:
            password += ambiguous_characters

        print(" ")

        i = 1
        while i <= num:
            i += 1
            pwd = "".join(random.sample(password, length))
            if test.validate_password_strength(pwd):
                encrypt_password(pwd, output_file)
                hit += 1
            else:
                i -= 1
                miss += 1
        print("Passwords accepted " + "{" + colored(str(hit), "green", attrs=['bold']) + "}." +
              " Passwords rejected " + "{" + colored(str(miss), "red", attrs=['bold']) + "}.")

    generate_password(add_symbols(input("Use symbols? (y/n): ")),
                      add_ambiguous_characters(input("Use ambiguous characters? (y/n): ")))
