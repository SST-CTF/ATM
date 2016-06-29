# -*- coding: utf-8 -*-
#
# ATM.py
# SST CTF's ATM program that will allows users to modify/view their ballances
# Copyright 2016 SST CTF
#

# Initial Imports
import sys
import csv
import os.path
import time

#Other setup
directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(directory, 'bank')

# Checks if given card number is within database
# Also check if pin matches entered card number
def checkCard(cardNumber):
    with open(filename, 'r') as f:
        next(f) # Skips first line because they are headers
        reader = csv.reader(f)
        userRow = 0
        for row in reader:
            row = list(map(float, row))
            userRow = userRow + 1
            # print row
            if cardNumber == int(row[0]):
                k = 1
                pin = int(input("Please enter your four digit pin: "))
                while k < 5:
                    if pin == int(row[1]):
                        print(userRow)
                        return userRow
                    else:
                        pin = int(input("Incorrect, please try again: "))
                        k = k + 1
                print("Access Denied!")
                sys.exit()
    print("This card does not exist, please try again.")
    return 0 # Possible add create new account in the future

# Check Balance function
def checkBalance(cardNumber,userRow):
    with open(filename, 'r') as f:
        next(f) # Skips first line because they are headers
        reader = csv.reader(f)
        k = 0
        for row in reader:
            k = k + 1
            if k == userRow:
                balance = row[2]
                print("\nYour balance is: $%s\n" % balance)
                return balance
        print("ERROR 1: BALANCE READ ERROR")


# Deposit function
def deposit(cardNumber, userRow):
    deposit_value = int(input("How much do you want to deposit? "))
    balance += deposit_value
    print("Your new balance is " + str(balance))

# Withdraw function
def withdrawal(cardNumber,userRow):
    balance = 50  # Make sure to get this from card numbers
    money_taken = int(input("How much money do you wish to withdraw? "))
    if balance - money_taken >= 0:
        balance -= money_taken
        print("Withdrawal successful.")
        print("Your new balance is " + str(balance) + " dollars.")
    else:
        print("Error: Not enough balance.")

# Program Begins (main menu and GUI)
print ("**********************************************")
print ("*********** Welcome to the SST ATM ***********")
print ("**********************************************")
userRow = 0
while userRow == 0:
    cardNumber = input("Please enter your credit card number or '1' to exit: ")
    if cardNumber == 1:
        sys.exit()
    userRow = checkCard(cardNumber)

# Selection is made here, each selection leads to a function above
selection = 0   # Define initially to run through loop
while selection < 4:
    selection = input("What would you like to do today?:\n 1. Check balance\n 2. Deposit Money\n 3. Withdraw Money\n 4. Exit\n\n")
    if selection is 1:  # Check Balance
        checkBalance(cardNumber,userRow)
    elif selection is 2:    # Deposit
        deposit(cardNumber,userRow)
    elif selection is 3:    #Withdraw
        withdrawal(cardNumber,userRow)
    elif selection is 4:    # Exit program
        print("Thank you, and have a nice day!")
sys.exit()