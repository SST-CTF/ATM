import sqlite3
import sys
import hashlib
import random
import uuid

conn = sqlite3.connect('bank.db')
c = conn.cursor()

def createAccount():
    counter = 1
    while counter == 1:
        cardNumber = (random.randrange(10000,99999))
        c.execute("SELECT Number FROM Account WHERE NUMBER = ?",(cardNumber,))
        check = c.fetchall()
        if check == []:
            counter = 0
            c.execute('INSERT INTO Account VALUES (?,0,0,0)',(cardNumber,))
            pinchange(cardNumber)
        else:
            counter = 1


def checkBalance(cardNumber):
    c.execute("SELECT balance FROM account WHERE Number = ?", (cardNumber,))
    new_balance = c.fetchall()
    new_balance1 = new_balance[0] #Turning array into tuple
    new_balance2 = new_balance1[0] #turnig tuple into number
    print('your balance is: ' + str(new_balance2))

def deposit(cardNumber):
    deposit_value = float(input("How much do you want to deposit? "))
    c.execute("SELECT Balance FROM Account WHERE Number = ?", (cardNumber,))
    new_balance = list(c.fetchall())
    new_balance = ''.join(str(e) for e in new_balance)
    new_balance = float(new_balance[1:-2])
    new_balance += deposit_value
    c.execute('UPDATE Account SET Balance = ? WHERE Number = ?', (new_balance, cardNumber))
    conn.commit()
    print("Your new balance is " + str(new_balance))

def withdraw(cardNumber):
    deposit_value = float(input("How much do you want to withdraw? "))
    c.execute("SELECT Balance FROM Account WHERE Number = ?", (cardNumber,))
    new_balance = list(c.fetchall())
    new_balance = ''.join(str(e) for e in new_balance)
    new_balance = float(new_balance[1:-2])
    if new_balance > deposit_value:
        new_balance -= deposit_value
        c.execute('UPDATE Account SET Balance = ? WHERE Number = ?', (new_balance, cardNumber))
        conn.commit()
        print("Your new balance is " + str(new_balance))
    else:
        print("Error: Not enough balance.")

def pinchange(cardNumber):
    pin_counter = 0
    while pin_counter == 0:
        new_pin = int(input("Enter new PIN code "))
        check_pin = int(input("Enter PIN code once more "))
        if new_pin == check_pin and len(str(new_pin)) == 4:
            salt = uuid.uuid4().hex
            c.execute("SELECT salt FROM Account WHERE Number = ?", (cardNumber,))
            c.execute('UPDATE Account SET Salt = ? WHERE Number = ?', (salt, cardNumber))
            new_pin = str(new_pin)
            new_pin = hashlib.sha256(new_pin.encode() + salt.encode()).hexdigest()
            c.execute("SELECT PIN FROM Account WHERE Number = ?", (cardNumber,))
            c.execute('UPDATE Account SET PIN = ? WHERE Number = ?', (new_pin, cardNumber))
            conn.commit()
            print("PIN updated")
            pin_counter = 1
            print("Your account number is: " + str(cardNumber))
        else:
          print("Please try again")

def checkCard(cardNumber):
    c.execute("SELECT Number, PIN FROM account WHERE Number = ?", (cardNumber,))
    row = c.fetchall()
    if row != []:
        raw = row[0]
        raw1 = str(raw[1])
        k = 1
        c.execute("SELECT Salt FROM account WHERE Number = ?", (cardNumber,))
        salt = c.fetchall()
        salt = salt[0]
        salt = salt[0]
        while k < 5:
            pin = str(input("Please enter your four digit pin: "))
            pin = hashlib.sha256(pin.encode() + salt.encode()).hexdigest()
            if pin == raw1:
                print ('CORRECT!')
                return 1
            else:
                k += 1
        print("Access Denied!")
        sys.exit()
    else:
        print("This card does not exist, please try again.")
        return 0

# Program Begins (main menu and GUI)
print("**********************************************\n*********** Welcome to the SST ATM ***********\n**********************************************")
cardExists = 0
while cardExists == 0:
    cardNumber = input("Please enter your credit card number or '2' to create a new account or '1' to exit: ")
    if int(cardNumber) == 1:
        sys.exit()
    elif int(cardNumber) == 2:
        createAccount()
    else:
        cardExists = checkCard(cardNumber)

# Selection is made here, each selection leads to a function above
selection = 0  # Define initially to run through loop
while int(selection) < 5:
    selection = input(
        "What would you like to do today?:\n 1. Check balance\n 2. Deposit Money\n 3. Withdraw Money\n 4. Change PIN number\n 5. Exit\n")
    if int(selection) == 1:  # Check Balance
        checkBalance(cardNumber)
    elif int(selection) == 2:  # Deposit
        deposit(cardNumber)
    elif int(selection) == 3:  # Withdraw
        withdraw(cardNumber)
    elif int(selection) == 4:  # Change
        pinchange(cardNumber)
    elif int(selection) == 5:  # Exit program
        print("Thank you, and have a nice day!")

c.close()
conn.close()
sys.exit()
