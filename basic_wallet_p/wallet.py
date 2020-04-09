import requests
import sys
import json
import os.path

if __name__ == '__main__':

    username = None

    def set_name(name):
        global username
        username = name
        f = open("my_id.txt", "w")
        f.write(name)
        f.close()

    def get_transactions():
        r = requests.get(url="http://localhost:5000/chain")
        try:
            data = r.json()
        except ValueError:
            print(f"Error: non-json respsonse: {r}")
            return

        all_blocks = data["chain"]
        transactions = []
        for block in all_blocks:
            for transaction in block["transactions"]:
                if transaction["sender"] == username or transaction["recipient"] == username:
                    transactions.append(transaction)
        return transactions

    if os.path.isfile("my_id.txt"):
        # Load the User ID file
        f = open("my_id.txt", "r")
        username = f.read()
        f.close()
    else:
        name = input("Please enter your name: ")
        set_name(name)

    print(f"Welcome, {username}")

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
            elif cmd in ["transactions", "t"]:
                transactions = get_transactions()
                print(json.dumps(transactions, indent=2))
        elif len(inputs) == 2:
            if inputs[0] == "name":
                set_name(inputs[1])
