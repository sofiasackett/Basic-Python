# This program accepts one integer between 1 and 10 and prints the Roman numeral

try:
    number = int(input("Please enter any integer between 1 and 10: "))
except:
    print("An error has occured: please try again and enter integers only: ")
else:
    if number >= 1 and number <= 10:
        if number ==1:
            print("I")
        if number ==2:
            print("II")
        if number ==3:
            print("III")
        if number ==4:
            print("IV")
        if number ==5:
            print("V")
        if number ==6:
            print("VI")
        if number ==7:
            print("VII")
        if number ==8:
            print("VIII")
        if number ==9:
            print("IX")
        if number ==10:
            print("X")
    else:
        print("An error has occured: please enter an integer from 1-10.")
