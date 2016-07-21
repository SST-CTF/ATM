#!user/bin/python3

import sys, random, os, hashlib, binascii

# Hashing function
def sha256hash(card, pin, salt_for_card, salt_for_pin):
    card_number = str(card)
    pin_number = str(pin)
    salt_for_card = str(salt_for_card)
    salt_for_pin = str(salt_for_pin)

    # Salting card and pin numbers

    salted_card_number = salt_for_card + card_number
    salted_pin_number = salt_for_pin + pin_number

    # Unhashing salted card and pin numbers

    sha256_card_number = hashlib.sha256(salted_card_number.encode()).hexdigest()
    sha256_pin_number = hashlib.sha256(salted_pin_number.encode()).hexdigest()
    
    # Return the numbers

    return sha256_card_number, sha256_pin_number

# Authorization Search
def search_account_security(auth_search):
    with open("accountsecurity.txt", "r") as accountsecurity:
        for line in accountsecurity:
            if auth_search in line:
                security = line
                auth_bool = True
                return security, auth_bool
        accountsecurity.close()
        # Error
        print("Error 2: Card number and pin number not found for user. Please try again.")
        sys.exit()

# Authorization Function
def auth():

    auth_bool = False

    # Getting account name
    name = input("What account name do you wish to access?\n> ")

    if user_check(name) is True:
        print("Error 6: Account not recognized. Please try again.\n")
        sys.exit()

    # Checking if name is in account info
    # If present, store the line it is on in info
    with open("accountinfo.txt", "r") as accountinfo:
        for line in accountinfo:
            if name in line:
                info = line
                break
        accountinfo.close()

    # Delimit info line by commas
    info_array = info.split(",")
    
    # Gather necessary authorization information
    card_number = input("What is your card number?\n> ")
    pin_number = input("What is your pin number?\n> ")
    salt_for_card = info_array[-2]
    salt_for_pin = info_array[-1].replace("\n","")

    # Get hashed authorization information
    sha256_card_number, sha256_pin_number = sha256hash(card_number, pin_number, salt_for_card, salt_for_pin)

    # Search for authorization information in accountsecurity.txt
    auth_search = sha256_card_number + "," + sha256_pin_number
    security, auth_bool = search_account_security(auth_search)

    # Delimit security by commas
    security_array = security.split(",")

    original_balance = float(security_array[-1])
    new_balance = float(security_array[-1])

    return original_balance, new_balance, sha256_card_number, sha256_pin_number, auth_bool

# Withdrawing money function
def withdraw(balance, amount):
    if amount > balance:
        print("Error 4: You do not have enough money in your account.\n")
    else:
        balance -= amount
    return balance

# Deposit money function
def deposit(balance, amount):
    balance += amount
    return balance

# Checking balance function
def check_balance(balance):
    print("You have " + str(balance) + " dollars.\n")

# Creating new account function
def create_account(name):

    # Check if user already exists
    if os.path.isfile("accountinfo.txt"):
        if user_check(name) is True:
            account_name = name
        else:
            # Error
            print("Error 1: That username has been taken. Please pick a different username.\n")
            sys.exit()
    else:
        account_name = name

    # Generate random card numbers and pin numbers
    card_number = random.randrange(99999999999, 999999999999)
    pin_number = random.randrange(999, 9999)

    # Generate random card salts and pin salts
    random_hex_card = binascii.b2a_hex(os.urandom(12))
    random_hex_pin = binascii.b2a_hex(os.urandom(12))
    salt_for_card = str(random_hex_card).replace("'","").replace("b","")
    salt_for_pin = str(random_hex_pin).replace("'","").replace("b","")

    # Store the account name and salts in accountinfo.txt
    with open("accountinfo.txt", "a") as accountinfo:
        accountinfo.write(account_name + "," + salt_for_card + "," + salt_for_pin + "\n")
        accountinfo.close()

    # Generate hashed card and pin numbers
    sha256_card_number, sha256_pin_number = sha256hash(card_number, pin_number, salt_for_card, salt_for_pin)   

    # Store hashed card and pin numbers in accountsecuirty.txt
    with open("accountsecurity.txt", "a") as accountsecurity:
        accountsecurity.write(str(sha256_card_number) + "," + str(sha256_pin_number) + ",0.0\n")
        accountsecurity.close()

    # Tell user information
    print("Please write down the follow information.\n")
    print("Your card number is " + str(card_number) + "\n")
    print("Your pin is " + str(pin_number) + "\n")

# Save function
def save(original_balance, new_balance, sha256_card_number, sha256_pin_number):

    # Replace old data with new data in account security.txt
    with open("accountsecurity.txt","r") as accountsecurity:
        old_account_security = accountsecurity.read()
        old_user_data = sha256_card_number + "," + sha256_pin_number + "," + str(original_balance) + "\n"
        new_user_data = sha256_card_number + "," + sha256_pin_number + "," + str(new_balance) + "\n"
        new_account_security = old_account_security.replace(old_user_data, new_user_data)
        accountsecurity.close()

    with open("accountsecurity.txt","w") as accountsecurity:
        accountsecurity.write(new_account_security)
        accountsecurity.close()

# User check function
def user_check(name):
    # If username does not exist in accountinfo.txt
    # Return True
    with open("accountinfo.txt") as usercheck:
        for line in usercheck:
            if name in line:
                return False
        usercheck.close()
        return True

def outer_menu():
    # First menu choice
    choice = input("Please enter '1' to authenticate.\nPlease enter '2' to open a new acccount.\nPlease enter '3' to exit.\n> ")

    # First Menu
    if choice is '1':
        original_balance, new_balance, sha256_card_number, sha256_pin_number, auth_bool = auth()
        inner_menu(original_balance, new_balance, sha256_card_number, sha256_pin_number)
    elif choice is '2':
        name = input("Please enter a unique username.\n> ")

        if "," in name:
            print("Error 5: Invald character. Please try again.")
            sys.exit()

        create_account(name)
    elif choice is '3':
        print("Thank you for using SST Test Bank. Please have a nice day.\n> ")
        sys.exit()
    else:
        print("Error 3: Invalid choice. Please try again.\n> ")

def inner_menu(original_bal, new_bal, sha256_card_num, sha256_pin_num):
    # Transfering over needed variables
    original_balance = float(original_bal)
    new_balance = float(new_bal)
    sha256_card_number = sha256_card_num
    sha256_pin_number = sha256_pin_num
    while True:
        # Second menu choice
        choice = input("Please enter '1' to deposit.\nPlease enter '2' to withdraw.\nPlease enter '3' to check balance.\nPlease enter '4' to save.\nPlease enter '5' to exit.\n> ") 
    
        # Second menu
        if choice is '1':
            amount = float(input("How much would you like to deposit?\n> "))
            new_balance = deposit(new_balance, amount)
        elif choice is '2':
            amount = float(input("How much would you like to withdraw?\n> "))
            new_balance = withdraw(new_balance, amount)
        elif choice is '3':
            check_balance(new_balance)
        elif choice is '4':
            save(original_balance, new_balance, sha256_card_number, sha256_pin_number)
        elif choice is '5':
            break
        else:
            print("Error 3: Invalid choice. Please try again.\n")

def main():
    print("***Welcome to the SST Test Bank***")
    while True:
        outer_menu()

main()
