#
# ATM.py
# SST CTF's ATM program that will allows users to modify/view their ballances
# © 2016 SST CTF
#

# Initial Imports
import sys

# Check Balance function
def check_balance(cardNumber):
    from account.txt import balance
    print(balance)

# Deposit function
def deposit(cardNumber):
    deposit_value = int(input("How much do you want to deposit? "))
    balance += deposit_value
    print("Your new balance is " + str(balance))

# Withdraw function
def withdrawal(cardNumber):
    balance = 50  # Make sure to get this from card numbers
    money_taken = int(input('How much money do you wish to withdrawal? '))
    if balance - money_taken >= 0:
        balance -= money_taken
        print("Withdrawal successful.")
        print("Your new balance is " + str(balance) + " dollars.")
    else:
        print("Error: Not enough balance.")

# Program Begins (main menu and GUI)
print ("***********************************\n**********")
print ("Welcome to the SST ATM **********\n***********************************")
cardNumber = input("Please enter your credit card number: ")
#
# Test if card number exists in textfile
#
pinNumber = input("Please enter your four digit pin: ")
#
# Test if pin matches card number
#

# Selection is made here, each selection leads to a function above
selection = 0   # Define initially to run through loop
while selection < 4:
    selection = input("What would you like to do today?:\n 1. Check balance\n 2. Deposit Money\n 3. Withdraw Money\n 4. Exit\n\n")
    if selection is 1:  # Check Balance
        checkBalance(cardNumber)
    elif selection is 2:    # Deposit
        deposit(cardNumber)
    elif selection is 3:    #Withdraw
        withdrawal(cardNumber)
    elif selection is 4:    # Exit program
        print("Thank you, and have a nice day!")
sys.exit()