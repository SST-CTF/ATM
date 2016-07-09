import sys

bal = 0

def checkbal():
    return(bal)

def withdraw(amnt):
    x = bal
    if amnt < x:
        x -= amnt
        print(x)
        return(x)
    else:
        print('You can\'t do that!')

def deposit(amnt):
    x = bal
    x += amnt
    print(x)
    return(x)

while True:
    user_input = input('What would you like to do?\nPress 1 to check your balance\nPress 2 to withdraw\nPress 3 to deposit\nPress 4 to exit the program\n')
    if user_input is 1:
        print(checkbal())
    elif user_input is 2:
        user_input2 = input('How much would you like to withdraw?\n')
        bal = withdraw(user_input2)
    elif user_input is 3:
        user_input3 = input('How much would you like to deposit?\n')
        bal = deposit(user_input3)
    elif user_input is 4:
        sys.exit()
    else:
        print('Invalid input')