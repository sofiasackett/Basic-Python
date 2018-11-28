#program to guess my favorite number with hints to guess a larger or smaller number

print("Try to guess my favorite number! \n")
actualNumber = 123
attempts = 0

while True:
    guessedNumber = input("Take a guess: ")
    attempts = attempts + 1
    try:
        guessedNumber = int(guessedNumber)
    except:
        print("ERROR: Please enter an integer.")
    else:
        if guessedNumber == actualNumber:
            print("Wow! You guessed correctly! It only took", attempts, "tries.")
            break
        elif guessedNumber < actualNumber:
            print("Incorrect! Guess a larger number.")
        else:
            print("Incorrect! Guess a smaller number.")
