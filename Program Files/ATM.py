# -*- coding: utf-8 -*-
#
# ATM.py
# SST CTF's ATM program that will allows users to modify / view their balances
# Copyright 2016 SST CTF
#

# Initial Imports
import sys
import csv
import os.path
import time
from random import randint

# Other setup
directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(directory, 'bank')
pin = 0

# Checks if given card number / pin is within database
def checkCard(cardNumber):
    with open(filename, 'r') as f:
        next(f) # Skips first line because they are headers
        reader = csv.reader(f)
        userRow = 0
        for row in reader:
            row = list(map(float, row))
            userRow = userRow + 1
            #print row
            if cardNumber == int(row[0]):
                k = 1
                pin = int(input("Please enter your four digit pin: "))
                while k < 5:
                    if pin == int(row[1]):
                        #print(userRow)
                        return (userRow, pin)
                    else:
                        pin = int(input("Incorrect, please try again: "))
                        k = k + 1
                print("Access Denied!")
                sys.exit()
    print("This card does not exist, please try again.")
    createAccount(cardNumber, )

# Create account function
def createAccount(cardNumber, pin):
    text = (str(cardNumber) + "," + str(pin) + ",0\n")
    with open(filename, 'a') as appendFile:
        appendFile.write(text)

# Balance overwite function
def replaceBalance(userRow, cardNumber, pin, balance):
    lines = open(filename, 'r').readlines()
    text = (str(cardNumber) + "," + str(pin) + "," + str(balance)+ "\n")
    lines[userRow] = text
    out = open(filename, 'w')
    out.writelines(lines)
    out.close()

# Check Balance function
def checkBalance(cardNumber, userRow):
    with open(filename, 'r') as f:
        next(f) # Skips first line because they are headers
        reader = csv.reader(f)
        k = 0
        for row in reader:
            k = k + 1
            if k == userRow:
                balance = row[2]
                return balance
        print("ERROR 1: BALANCE READ ERROR")
        sys.exit()

# Deposit function
def deposit(cardNumber, userRow, balance):
    depositValue = float(input("How much do you want to deposit? "))
    balance = float(balance) + depositValue
    print("Your new balance is $%s" % str(balance))
    replaceBalance(userRow, cardNumber, pin, balance)
    return balance


# Withdraw function
def withdrawal(cardNumber, userRow, balance):
    withdrawalValue = float(input("How much money do you wish to withdraw? "))
    if float(balance) - withdrawalValue >= 0:
        balance = float(balance) - float(withdrawalValue)
        print("Withdrawal successful.")
        print("Your new balance is: $%s" %balance)
        replaceBalance(userRow, cardNumber, pin, balance)
        return balance
    else:
        print("ERROR 2: Not enough money to withdraw.")
        return float(balance)

# Clear console when needed
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# Program Begins (main menu and GUI)
cls()
print ("**********************************************")
print ("*********** Welcome to the SST ATM ***********")
print ("**********************************************")
userRow = 0
while userRow == 0:
    cardNumber = input("Enter your credit card number, '1' to exit, or '0' to create a new account: \n")
    if cardNumber == 1:
        sys.exit()
    elif cardNumber == 0:
        cardNumber = input("To create an account please enter a FIVE DIGIT card number: ")
        pin = randint(1001,9999)
        print("Your pin is: %s" % pin)
        createAccount(cardNumber, pin)
        userRow, pin = (checkCard(cardNumber))
    else:
        userRow, pin = (checkCard(cardNumber))
balance = checkBalance(cardNumber,userRow)

# Selection is made here, each selection leads to a function above
selection = 0   # Define initially to run through loop
while selection < 4:
    selection = input("\nWhat would you like to do today?:\n 1. Check balance\n 2. Deposit Money\n 3. Withdraw Money\n 4. Exit\n\n")
    if selection is 1:  # Check Balance
        print("Your balance is: $%s" % balance)
    elif selection is 2:    # Deposit
        balance = deposit(cardNumber, userRow, balance)
    elif selection is 3:    #Withdraw
        balance = withdrawal(cardNumber, userRow, balance)
    elif selection is 4:    # Exit program
        print("Thank you, and have a nice day!")
sys.exit()

# <> Credits <>
# Otakar A. - Primary Developer
# Andrew Q. - Withdraw Function
# Stan L.   - Deposit Function
# Tamir E.  - Initial Check Balance Function
#
# EOF