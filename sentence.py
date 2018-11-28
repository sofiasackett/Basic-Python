#create a sentence from a random amount of user-entered words

from random import *
n = randint(5, 12)

count = n
file = open("sentence.txt", "w")
while count !=0:
    count = count - 1
    word = input("Enter a word here: ")
    word = word.upper()
    file.write(str(word) +" ")
file.close()

file = open("sentence.txt", "r")
print(file.read(), "!")
