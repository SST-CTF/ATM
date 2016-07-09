bal = 0

def checkbal():
    return(bal)

def withdraw(amnt):
    global bal
    bal -= amnt

def deposit(amnt):
    global bal
    bal += amnt

user_input = input('What would you like to do?\nPress 1 to check your balance\nPress 2 to withdraw\nPress 3 to deposit')
if user_input is 1:
    checkbal()
elif user_input is 2:
    user_input2 = input('How much would you like to withdraw?\n')
    withdraw(user_input2)
elif user_input is 3:
    user_input3 = input('How much would you like to deposit?\n')
    deposit(user_input3)
else:
    print('Invalid input')