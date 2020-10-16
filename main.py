# MAIN FILE
# This is what we are going to interact with! You can think of this file as the conductor in an orchestra
# It imports all the other files and plays them only when needed

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
        file.close()
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

def retrieve_subjects():
    file = open("subjects.txt", "r")
    return file.readline().split(',')

def main():
    global username
    if not path.exists("config.ini"):
        setup.initialize()
    else:
        print("Configuration File Found!\n")
        if load_file():
            password = prompt_password()
            scraper.run_scraper(username, password)
            scraper.get_announcements()
            scraper.open_subjects(retrieve_subjects())
        else:
            print("Something went wrong... try deleting 'config.ini' and setup again!")
        
if __name__ == "__main__":
    main()