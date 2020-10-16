# SETUP FILE
# This file creates the config.ini that will store our encrypted password
# It will only be run once during initialization, but it is handy to keep it here in case you want to reset your password 
# or if something ever goes wrong!

# Remember to import encryption(handles encryption/decryption) & json(to specifically write the encrypted data into config.ini)
import encryption
import json

username = ""
password = ""

def initial_prompt():
    # Prompt the user for username & password

def masterpw_prompt():
    # Prompt the user for master password which will be used as a key to decrypt the real password

# I've had people run this file directly (which is not what we want!) so I created a function that prints a warning and exits when
# this file is run
def warning():
    print("You shouldn't be running this file directly! Please run main.py!")     
    
# This basically means:
# If this file is run directly, run warning() function
if __name__ == "__main__":
    warning()
    