# Sofia Sackett
# This program acts as a magic-8 ball, and replies with one of ten original responses

# Import necessary modules
import random
import time

# Get user input
print("To begin using this Magic 8-ball, think of a yes or no question.")
ready = input("When you're ready, press enter to receive your answer!")

# Create a function which selects reply
def reply():
    number = random.randint(1, 10)
    if number == 1:
        return("Only time will tell.")
    elif number == 2:
        return("I'm not sure yet.")
    elif number == 3:
        return("Whatever you think is best.")
    elif number == 4:
        return("Of course!")
    elif number == 5:
        return("Yes, indeed!")
    elif number == 6:
        return("You bet!")
    elif number == 7:
        return("Indubitably.")
    elif number == 8:
        return("No dice.")
    elif number == 9:
        return("Not in this lifetime.")
    else:
        return("No way, José.")

# Output answer
print("Thinking...\n")
time.sleep(2)
print(reply())
