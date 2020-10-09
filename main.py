import setup, encryption
from os import path
import json

username = ""
password = ""
data = ""

def load_file():
    try:
        global username, data
        file = open("config.ini", "r")
        username = file.readline()
        data = file.readline()
        return True
    except:
        return False

def prompt_password():
    success = False
    while not success:
        key = input("Enter master password: ") 
        try:
            decrypted_data = encryption.decrypt(json.loads(data), key)
            print(decrypted_data)
            success = True
        except:
            print("\nWrong password!\n")

def main():
    if not path.exists("config.ini"):
        setup.initialize()
    else:
        print("Configuration File Found!\n")
        load_file()
        prompt_password()
        
if __name__ == "__main__":
    main()