import sys

print ("\n\n\n\n\n\n\n********************************************\n********** Welcome to the SST ATM **********\n********************************************")
cardNumber = input("Please enter your credit card number: ")
# TEST IF CARD IS VALID
pinNumber = input("Please enter your four digit pin: ")
# TEST IF PIN MATCHES

#Check Balance function here

#Deposit function here
def deposit():
    global balance
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

selection = 0
while selection < 4:
    selection = input("What would you like to do today?:\n 1. Check balance\n 2. Deposit Money\n 3. Withdraw Money\n 4. Exit\n\n")
    if selection is 1:  # The if keyword starts out the if elif else combo. Make sure you have a colon after the condition.
        checkBalance(cardNumber)
    elif selection is 2:  # The is keyword is similar to ==. It tests if something is equal to another thing. elif is optional.
        deposit(cardNumber)
    elif selection is 3:  # You can have no elif, or many elif statements
        withdrawal(cardNumber)
    elif selection is 4:  # You can have no elif, or many elif statements
        print("Thank you, and have a nice day!")
        import sys
sys.exit()



