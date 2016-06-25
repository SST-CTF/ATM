# Single line comments start with a hash
# The print function prints out a string

print ("test")

# Numbers can be
print (3 + 4)  # added
print (3 - 4)  # subtracted
print (3 * 4)  # multiplied
print (3 ** 4)  # power
print (3 / 4)  # divided
print (3 // 4)  # divided but rounded down
print (3 % 4)  # used to find the remainder (modulus)
# Follows order of operation

# Numbers can be stored in strings
test = 3
print (test + 4)

# Strings are stored in quotes (single or double)
test = "test"  # Strings can be stored in variables
test = 'test'

donot = 'don\'t'  # You can use a backslash to treat the next symbol as normal text
print (r'C:\nudes')  # You can add an r to disregard the formatting for the whole string (useful with file paths)

# You can use math operators on strings
print (test + donot)  # This would print out testdon't
print (test * 5)  # This would print out testtesttesttesttest

# You can find a character within a string using an array
test = "TestString"
print (test[0])  # This would print 'T' as arrays start counting from 0
print (test[-2])  # You can start from the back using negative values. This would print out the 'n'.

# You can print out a certain part of a string using a colon and two numbers. This prints out 'es'.
# From test[1] to test[3] without printing test[3]
print (test[1:3])

# Including a blank value means it will start from the beginning/end
print (test[:3])  # Tes
print (test[3:])  # tString
print (test[:])  # TestString

# The length function finds the length of a string
print(len('test'))  # 4

# You can store many of the same data type in one variable using a list/array
test = [20, 21, 24, 27]

# You can extract a certain value out of the list using the same technique above
print (test[2])  # 24
print (test[1:3])  # [21, 24]

# You can append to the list using .append()
test.append(120)
print (test)  # [20, 21, 24, 27]

# You can also just set parts of the list equal to something else
test[1:3] = [0, 0, 0, 0, 0]
print (test)  # [20, 0, 0, 0, 0, 0, 27, 120]
test[:] = []
print (test)  # []

# A simple function is the if elif else combo
test = 4

if test < 3:  # The if keyword starts out the if elif else combo. Make sure you have a colon after the condition.
    print("test is less than 3")  # This executes if the if statement is true
elif test is 4:  # The is keyword is similar to ==. It tests if something is equal to another thing. elif is optional.
    print ("test is 4")
elif test is 3:  # You can have no elif, or many elif statements
    print ("test is 3")
else:  # Else is a catchall statement. If no above statements are true, print the else. The else statement is optional.
    print ("test is above 4")
# Make sure your indentations are correct. Indentation shows nesting.

test = [21, 33, 35, 26]

# For loops can loop through a list. Assign a random variable (k in this case).
for k in test:  # k will be a placeholder for each item
    # The first time it loops, k = 21. Then k = 33. etc...
    print k  # The result is the whole list being printed.

# You can also loop through only a certain part of the list
for k in test[1:3]:
    print k  # The result is 33 and 35

# You can use for loops in conjunction with range
for k in range(10):
    print k  # This would print 0 through 9

# This is useful for running code many times
for k in range(10):
    print "Andrew is awesome!"  # This statement would print 10 times.

# There are three arguments for the range function
print(range(10))  # With 1 argument, it is just printing x numbers starting from 0. In this case, [0-9]
print(range(3, 10))  # With 2 arguments, it is printing within the stated range. In this case, [3-9]
print(range(3, 10, 2))  # With 3 arguments, it is stepping within the stated range.
# In the above, it will step by 2s from #3 to 9. The output will be [3, 5, 7, 9]

# The while loop is much simpler. It runs the code while the condition is still true.
test = 0

while test < 4:  # While test is less than 4
    print(test)  # Print test
    test += 1  # And increment test by 1. += -= *= /= %= all do the operation, then set the variable to the outcome
# Note you increment the variable test, in this case, in order to avoid an infinite loop.

# We can use 'break' to improve the efficiency of our loops. Break simply breaks out of the loop.
test = 34

for n in range(1000):  # We loop 1000 times
    if n is test:  # If we find that test is equal to n
        print(n, "is test")  # We print n
        break  # Now that we know the value of test, we don't need to run the loop anymore.
        # We break out of the loop to improve efficiency.

# Fun fact! In order to print out an integer along with a string, use a comma not a plus sign.
''' (Triple quotes are a way to multi-line comment)
print(test + "test")  # This would error
'''
print (test, "test")  # This would not error

# 'Continue' is like break, except it doesn't completely break out of the loop.
test = [2, 5, 8, 10]

for n in range(1, 11):  # We set up a loop going from 1 to 10
    if n in test:  # If the number n is in the test list
        continue  # Continue, meaning skip all other statements in the loop (print in this case)
        # Then continue with the loop for the next n
    print(n)  # Print n


# This code would print out all numbers from 1 to 10 that are not contained in the test list.
# 1, 3, 4, 6, 7, 9

# Functions are a great way of reusing code without having to rewrite the code every time.

def testfunction():  # You must first define the function you want
    print("This is a test function.")  # Then you tell what the function does
    print("Pretty cool right?")


testfunction()  # You can call the function by simply writing its name.


# Functions can also take extra information, or arguments
def bitcoin_to_usd(bitcoin):  # Put the argument needed in the parentheses, in this case 'bitcoin'
    usd = bitcoin * 607.18
    print(usd)


bitcoin_to_usd(3)  # You can call the function the same way as the last time. Just remember to include the argument.


# Returning values is more flexible than printing values
def bitcoin_to_usd(bitcoin):
    usd = bitcoin * 607.18
    return usd  # Instead of printing USD, we now return USD.


test = bitcoin_to_usd(3.14)  # This allows us to do many things like setting the return value equal to another variable
print (test, "USD")


# Having a default value for arguments prevents the program from erroring when no argument is given.
def bitcoin_to_usd(bitcoin=0):  # We set bitcoin by default to 0.
    usd = bitcoin * 607.18
    return usd


test = bitcoin_to_usd()  # If we call this function without entering an argument
print (test, "USD")  # The program no longer errors, but rather gives us an output of 0.


# There are two basic rules about variables.

def variable1():
    print(test)


test = 1

variable1()  # The variable a function calls must be above the function in order to work.
# Test is defined before we called the function, so this code is not error.

# This would error as test was not defined before the variable1 function was called:
'''
def variable1():
    print(test)

variable1()

test = 1
'''

# Rule two, a variable declared in a function is a local variable. It cannot be utilized outside of that function.
# This would error as test is defined in variable1, so it cannot be used in variable2.
'''
def variable1():
    test = 1
    print(test)


def variable2():
    print(test)
'''


# You can have many arguments in a function.
def sentencify(noun="Andrew", verb="is", adjective="awesome"):
    print(noun, verb, adjective)

sentencify()  # Since we have default arguments, this does not error.
sentencify("Nobody", "likes", "Otakar")  # We can also input our own arguments,
sentencify(noun="Life", adjective="meaningless")  # If you want to pass only a few arguments, you need to use keywords.
sentencify(noun="Nobody")  # Here is another example
# The keywords are the name of the arguments. In this case: noun, verb, and adjective.

# If there is an unknown amount of arguments, you can use *args.


def addition(*args):  # '*args' packs all arguments into a list named args.
    total = 0
    for n in args:  # We add up all the numbers in args
        total += n
    return total

total = addition(1, 4, 65, 7, 34, 5, 67, 7)  # We can now use as many arguments as we please.
print(total)

# You can unpack as well as pack arguments


def sentencify(noun="Andrew", verb="is", adjective="awesome"):
    print(noun, verb, adjective)

sentence1 = ["Life", "Is", "Unfair"]

sentencify(sentence1[0], sentence1[1], sentence1[2])  # The normal method is tedious
sentencify(*sentence1)  # We can unpack the arguments and do the same thing much quicker by adding an asterisk