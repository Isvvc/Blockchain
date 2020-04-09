import requests
import sys
import json
import os.path

if __name__ == '__main__':

    username = None

    if os.path.isfile("my_id.txt"):
        # Load the User ID file
        f = open("my_id.txt", "r")
        username = f.read()
        f.close()
    else:
        name = input("Please enter your name: ")
        f = open("my_id.txt", "w")
        f.write(name)
        f.close()

    def set_name(name):
        global username
        username = name
        f = open("my_id.txt", "w")
        f.write(name)
        f.close()

    while True:
        cmd = input("-> ")
        inputs = cmd.split()    

        if len(inputs) == 1:
            if cmd == "q":
                break
            elif cmd in ["h", "help"]:
                print("Commands:")
                print("h, help: Show this help menu")
                print("name: Show the current username")
                print("name [new_name]: Set a new username")
                print("q: Quit the program")
            elif cmd == "name":
                print(f"Current user: {username}")
        elif len(inputs) == 2:
            if inputs[0] == "name":
                set_name(inputs[1])
