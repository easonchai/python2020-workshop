import encryption
from os import path

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
    user_config.write(username)
    user_config.write(encrypted_data)
    user_config.close()
    print("Configuration File Written!")

def main():
    if not path.exists("config.ini"):
        initial_prompt()
        masterpw_prompt()
    else:
        print("Configuration File Found!\n")
        file = open("config.ini", "r")
        username = file.readline()
        data = file.readline()
        print(username)
        print(data)
        key = input("Enter master password: ")
        decrypted_data = encryption.decrypt(data, key)
        print(decrypted_data)
if __name__ == "__main__":
    main()