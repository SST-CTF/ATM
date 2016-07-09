#!user/bin/python3

import sys, random, os, hashlib, binascii

auth_bool = False
user_old_balance = 0.0
user_balance = 0.0
user_sha256_card_num = ""
user_sha256_pin = ""

def auth():
    name = input("What account name do you wish to access?\n")
    with open("accountinfo.txt", "r") as accountinfo:
        for line in accountinfo:
            if name in line:
                info = line
                break
        accountinfo.close()
    info_array = info.split(",")
    
    card_number = input("What is your card number?\n")
    pin = input("What is your pin number?\n")
    salted_card_num = info_array[1] + card_number
    salted_pin = str(info_array[2] + pin).replace("\n","")
    sha256_card_num = hashlib.sha256(salted_card_num.encode()).hexdigest()
    sha256_pin = hashlib.sha256(salted_pin.encode()).hexdigest()
    auth_search = sha256_card_num + "," + sha256_pin

    with open("accountsecurity.txt", "r") as accountsecurity:
        for line in accountsecurity:
            if auth_search in line:
                security = line
                global auth_bool
                auth_bool = True
                break
        accountsecurity.close()

    security_array = security.split(",")

    global user_old_balance, user_balance, user_sha256_card_num, user_sha256_pin
    user_old_balance = float(security_array[2])
    user_balance = float(security_array[2])
    user_sha256_card_num = sha256_card_num
    user_sha256_pin = sha256_pin

def withdraw(amount):
    global user_balance
    if amount > user_balance:
        print("You do not have enough money.")
    else:
        user_balance -= amount

def deposit(amount):
    global user_balance
    user_balance += amount

def check_balance():
    global user_balance
    print("You have " + str(user_balance) + " dollars.")

def create_account(name):
    card_number = random.randrange(99999999999, 999999999999)
    pin = random.randrange(999, 9999)
    if os.path.isfile("accountinfo.txt"):
        if user_check(name) is True:
            acc_name = name
        else:
            print("That username has been taken. Please pick a different username.")
    else:
        acc_name = name
        print(acc_name)

    salt_card_num = binascii.b2a_hex(os.urandom(12))
    salt_pin = binascii.b2a_hex(os.urandom(12))
    salt_card_num_fix = str(salt_card_num).replace("'","").replace("b","")
    salt_pin_fix = str(salt_pin).replace("'","").replace("b","")

    with open("accountinfo.txt", "a") as accountinfo:
        accountinfo.write(acc_name + "," + salt_card_num_fix + "," + salt_pin_fix + "\n")
        accountinfo.close()
    salted_card_num = salt_card_num_fix + str(card_number)
    salted_pin = salt_pin_fix + str(pin)
    sha256_card_num = hashlib.sha256(salted_card_num.encode()).hexdigest()
    sha256_pin_num = hashlib.sha256(salted_pin.encode()).hexdigest()

    with open("accountsecurity.txt", "a") as accountsecurity:
        accountsecurity.write(str(sha256_card_num) + "," + str(sha256_pin_num) + ",0.0\n")
        accountsecurity.close()
    print("Please write down the follow information.\n")
    print("Your card number is " + str(card_number) + "\n")
    print("Your pin is " + str(pin) + "\n")

def save_exit():
    with open("accountsecurity.txt","r") as accountsecurity:
        olddata = accountsecurity.read()
        newdata = olddata.replace(user_sha256_card_num + "," + user_sha256_pin + "," + str(user_old_balance) + "\n", user_sha256_card_num + "," + user_sha256_pin + "," + str(user_balance) + "\n")
        accountsecurity.close()

    with open("accountsecurity.txt","w") as accountsecurity:
        accountsecurity.write(newdata)
        accountsecurity.close()


def user_check(name):
    if name in open("accountsecurity.txt").read():
        return True
    
def main():

    print("Welcome to the SST Test Bank!\n")
    choice = input("Please enter '1' to authenticate, '2' to open a new account, or '3' to exit\n")
    
    if choice is '1':
        auth()
        if auth_bool is True:
            choice2 = input("Please enter '1' to deposit, '2' to withdraw, '3' to check balance, or '4' to exit\n")
            if choice2 is '1':
                amount = input("How much would you like to deposit?\n")
                deposit(amount)
            elif choice2 is '2':
                amount = input("How much would you like to withdraw?\n")
                withdraw(amount)
            elif choice2 is '3':
                check_balance()
            elif choice2 is '4':
                sys.exit()
            else:
                print("Invalid choice\n")
    elif choice == '2':
        name = input("Please enter a username\n")
        create_account(name)
    elif choice == '3':
        print("Thank you - Please have a nice day\n")
        sys.exit()
    else:
        print("Invalid choice")
        print(choice)

main()
