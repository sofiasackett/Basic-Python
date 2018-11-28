#This program will calculate the square root of a 3 digit integer

#input and import math
number = input("Please enter any positive 3-digit number: ")
import math

#exception handling
try:
    number = int(number)
except:
    print("An error has occurred: please try again and enter a 3-digit integer.")
else:
    if number in range(100, 999):
        sqroot = math.sqrt(number)
        print(sqroot)
    else:
        print("An error has occured: please enter a digit between 100 and 999.")
