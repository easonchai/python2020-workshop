import setup, encryption, scraper
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
    decrypted_data = ""
    while not success:
        key = input("Enter master password: ") 
        try:
            decrypted_data = encryption.decrypt(json.loads(data), key)
            success = True
        except:
            print("\nWrong password!\n")

    return decrypted_data

def main():
    global username
    if not path.exists("config.ini"):
        setup.initialize()
    else:
        print("Configuration File Found!\n")
        if load_file():
            password = prompt_password()
            scraper.run_scraper(username, password)
        else:
            print("Something went wrong... try deleting 'config.ini' and setup again!")
        
if __name__ == "__main__":
    main()