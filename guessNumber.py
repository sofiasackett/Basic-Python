# This program asks the user to try to guess my favorite number
# It will provide prompts for the user to guess higher or lower

my_num = 99
guess = False
count = 0
while guess == False:
    try:
        guess = int(input("Guess my favorite number! "))
    except:
        print("An error has occured. Only enter numeric values.")
    else:
        count = count + 1
        if guess == my_num:
            guess = True
            print("Correct! It took you", count, "attempts to guess my favorite number.")
        elif guess > my_num:
            print("Guess lower!")
            guess = False
        elif guess < my_num:
            print("Guess higher!")
            guess = False
