import encryption
import json

username = ""
password = ""

def initial_prompt():
    global username, password
    correct = "n"
    while correct.lower() != "y":
        username = input("Enter username: ")
        password = input("Enter password: ")
        print("")
        print("Username:", username)
        print("Password:", password)
        correct = input("\nAre you sure your details are correct? [y/n] : ")

def masterpw_prompt():
    global username,password
    match = False
    key = ""
    while match == False:
        print("\nTo encrypt your password, please enter a master password that will be used to access your login! This should not\
        be the same as your original password.")
        key = input("Enter master password: ")
        check = input("Enter master password again: ")
        if key == check:
            match = True
        else:
            print("Password does not match!\n")
    
    encrypted_data = encryption.encrypt(password, key)
    user_config = open("config.ini", "w")
    user_config.write(username + "\n")
    user_config.write(json.dumps(encrypted_data))
    user_config.close()
    print("Configuration File Written!")

def initialize():
    initial_prompt()
    masterpw_prompt()

def warning():
    print("You shouldn't be running this file directly! Please run main.py!")     
    
if __name__ == "__main__":
    warning()
    