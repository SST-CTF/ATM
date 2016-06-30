import sqlite3
import sys


conn = sqlite3.connect('bank.db')
c = conn.cursor()


def checkBalance(cardNumber):
    c.execute("SELECT balance FROM account WHERE Number = ?", (cardNumber,))
    new_balance = c.fetchall()
    new_balance1 = new_balance[0] #Turning array into tuple
    new_balance2 = new_balance1[0] #turnig tuple into number
    print('your balance is: ' + str(new_balance2))

def deposit(cardNumber):
    deposit_value = int(input("How much do you want to deposit? "))
    c.execute("SELECT Balance FROM Account WHERE Number = ?", (cardNumber,))
    new_balance = list(c.fetchall())
    new_balance = ''.join(str(e) for e in new_balance)
    new_balance = new_balance[1:-2]
    new_balance = int(new_balance[:])
    new_balance += deposit_value
    c.execute('UPDATE Account SET Balance = ? WHERE Number = ?', (new_balance, cardNumber))
    conn.commit()
    print("Your new balance is " + str(new_balance))

def withdraw(cardNumber):
    deposit_value = int(input("How much do you want to withdraw? "))
    c.execute("SELECT Balance FROM Account WHERE Number = ?", (cardNumber,))
    new_balance = list(c.fetchall())
    print(cardNumber)
    new_balance = ''.join(str(e) for e in new_balance)
    new_balance = new_balance[1:-2]
    new_balance = int(new_balance[:])
    if new_balance > deposit_value:
        new_balance -= deposit_value
        c.execute('UPDATE Account SET Balance = ? WHERE Number = ?', (new_balance, cardNumber))
        conn.commit()
        print("Your new balance is " + str(new_balance))
    else:
        print("Error: Not enough balance.")

def checkCard(cardNumber):
    print(cardNumber)
    c.execute("SELECT Number, PIN FROM account WHERE Number = ?", (cardNumber,))
    row = c.fetchall()
    if row != []:
        raw = row[0]
        raw1 = int(raw[1])
        k = 1
        pin = (int(input("Please enter your four digit pin: ")))
        while k < 5:
            if pin == raw1:
                print ('CORRECT!')
                return 1
            else:
                pin = int(input("Incorrect, please try again: "))
                k += 1
        print("Access Denied!")
        sys.exit()
    else:
        print("This card does not exist, please try again.")
        return 0  # Possible add create new account in the future


# Program Begins (main menu and GUI)
print("**********************************************")
print("*********** Welcome to the SST ATM ***********")
print("**********************************************")
cardExists = 0
while cardExists == 0:
    cardNumber = input("Please enter your credit card number or '1' to exit: ")
    if int(cardNumber) == 1:
        sys.exit()
    else:
        cardExists = checkCard(cardNumber)

# Selection is made here, each selection leads to a function above
selection = 0  # Define initially to run through loop
while int(selection) < 4:
    selection = input(
        "What would you like to do today?:\n 1. Check balance\n 2. Deposit Money\n 3. Withdraw Money\n 4. Exit\n\n")
    if int(selection) == 1:  # Check Balance
        checkBalance(cardNumber)
    elif int(selection) == 2:  # Deposit
        deposit(cardNumber)
    elif int(selection) == 3:  # Withdraw
        withdraw(cardNumber)
    elif int(selection) == 4:  # Exit program
        print("Thank you, and have a nice day!")
  #  elif selection is 5:  # Change
        #change_account(cardNumber)
sys.exit()
