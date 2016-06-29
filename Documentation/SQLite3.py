import sqlite3
import sys
conn = sqlite3.connect('bank.db')
c = conn.cursor()

def checkCard():
    cardNumber = (int(input("Enter account number: ")),)
    c.execute("SELECT Number, PIN FROM account WHERE Number = ?", cardNumber)
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

checkCard()

#create_table()
#data_entry()

