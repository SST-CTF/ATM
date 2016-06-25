import sys

print ("\n\n\n\n\n\n\n********************************************\n********** Welcome to the SST ATM **********\n********************************************")
cardNumber = input("Please enter your credit card number: ")
# TEST IF CARD IS VALID
pinNumber = input("Please enter your four digit pin: ")
# TEST IF PIN MATCHES

#Check Balance function here
def check_balance(cardNumber):
    from account.txt import balance
    print(balance)

#Deposit function here
def deposit(cardNumber):
    balance = 4
    deposit_value = int(input("How much do you want to deposit? "))
    balance += deposit_value
    print("Your new balance is " + str(balance))

# Withdrawl function here
def withdrawal(cardNumber):
    balance = 50  # Make sure to get this from card numbers
    money_taken = int(input('How much money do you wish to withdrawal? '))
    if balance - money_taken >= 0:
        balance -= money_taken
        print("Withdrawal successful.")
        print("Your new balance is " + str(balance) + " dollars.")
    else:
        print("Error: Not enough balance.")

# Selection is made here, each selection leads to a function above
selection = 0
while selection < 4:
    selection = input("What would you like to do today?:\n 1. Check balance\n 2. Deposit Money\n 3. Withdraw Money\n 4. Exit\n\n")
    if selection is 1: 
        checkBalance(cardNumber)
    elif selection is 2: 
        deposit(cardNumber)
    elif selection is 3: 
        withdrawal(cardNumber)
    elif selection is 4: 
        print("Thank you, and have a nice day!")
        import sys
sys.exit()
