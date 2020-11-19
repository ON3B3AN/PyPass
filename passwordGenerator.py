import passwordStrengthTest as test
from termcolor import colored
from encryptDecrypt import *
# import encryptDecrypt as crypt
import random
from pathlib import Path
import os


def generate_passwords():
    generate_key()
    # output_file = get_output_file_path()
    output_file_path = get_output_file_path()
    output_file = open(f"{output_file_path}{filePathSeparator}password_list.bin","wb")
    print("[passwordGenerator.py] The output_file is:", output_file)
    uppercase_letters = "ABCDEFGHIJKLNMOPQRSTUVWXYZ"
    lowercase_letters = uppercase_letters.lower()
    digits = "0123456789"
    ambiguous_characters = "{}[]()/\\\'\"`~,;:.<> "
    symbols = "@#$%!&*"

    upper, lower, nums = True, True, True

    numLoopStop = False
    while not numLoopStop:
        try:
            number = int(input("Enter the number of passwords to generate: "))
        except:
            print("[passwordGenerator.py] You did not enter a valid Integer; please try again!")
            continue

        if not number > 1:
            print("[passwordGenerator.py] Number of passwords must be more than 1! Please try again...")
        else:
            numLoopStop = True

    lenLoopStop = False
    while not lenLoopStop:
        try:
            length = int(input("Enter your desired password length (min: 8): "))
        except:
            print("[passwordGenerator.py] You did not enter a valid Integer; please try again!")
            continue

        if length < 8:
            print("[passwordGenerator.py] Length of password is", length, ", which is less than 8! Please try again...")
        else:
            lenLoopStop = True


    def add_symbols(answer):
        if answer.upper() == "Y" or answer.lower() == "y":
            syms = True
        elif answer.upper() == "N" or answer.lower() == "n":
            syms = False
        else:
            print("Input not recognized")
            syms = add_symbols(input("Use symbols? (y/n): "))
        return syms

    def add_ambiguous_characters(answer):
        if answer.upper() == "Y" or answer.lower() == "y":
            chars = True
        elif answer.upper() == "N" or answer.lower() == "n":
            chars = False
        else:
            print("Input not recognized")
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
        while i <= number:
            i += 1
            pwd = "".join(random.sample(password, length))
            if test.validate_password_strength(pwd):
                encrypt_password(pwd, output_file)
                hit += 1
            else:
                i -= 1
                miss += 1
        print("\nPasswords accepted " + "{" + colored(str(hit), "green", attrs=['bold']) + "}." +
              " Passwords rejected " + "{" + colored(str(miss), "red", attrs=['bold']) + "}." + "\n")

    generate_password(add_symbols(input("Use symbols? (y/n): ")),
                      add_ambiguous_characters(input("Use ambiguous characters? (y/n): ")))

