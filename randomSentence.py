# This program will create a sentence based on a random number of words

# Import random and greet user
import random
num = random.randint(5, 12)
print("Please enter", num, "random words...\n")

# Set accumulator variable to 0 and list to empty
count = 0
sentence = []

# Create a while loop to add words to the list 
while count < num:
    word = input("Input any word: ")
    sentence.append(str(word))
    count = count + 1

# Print sentence in all caps with space between words and exclamation mark
message = " ".join(sentence)
print(message.upper(), "!")

