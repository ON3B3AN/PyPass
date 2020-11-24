# PyPass
A Password Manager built in Python that generates encrypted passwords and stores them in a database for easy access.

## Authors
Travis Thayer & Sal Trupiano

## Project Information
Developed for CSI-3680: Script Programming at Oakland University, School of Engineering and Computer Science

## Project Key Features
* Accepts a CSV file of usernames and websites created by the user
  * (Format: username, website)
* Generates and appends encrypted passwords for each row in the CSV file with the following specifications:
  * AES 128-Bit Encryption secured with a Private Key encoded in Base_32
    * Application stores the private key in a user-defined removable media device for two-factor authentication.
  * User defines the following password specifications:
    * Length (minimum 8 characters)
    * Use of symbols and ambiguous characters
* Stores data from CSV, complete with encrypted passwords into a SQLite Database.
* Displays complete dictionary to the user (queries DB and decrypts each password).
* Input Validation for ALL user input (file paths, password specifications, etc.)

## Supported Operating Systems
* Windows
* macOS
* Linux

## Required Python Libraries
* Cryptography
* Platform
* Termcolor
* JSON
* Pathlib
* OS
* Sys
* Random
* CSV
* SQLite3
* RE
