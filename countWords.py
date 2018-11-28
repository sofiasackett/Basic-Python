# This program will count the number of words in a text input
text = str(input("Enter a sentence here: "))
word = text.split()
num_words = len(word)
print("The text you entered contains", num_words, "words.")
