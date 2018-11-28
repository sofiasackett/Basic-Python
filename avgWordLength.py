# This program will calculate the average word length in a text input
text = str(input("Enter a sentence here: "))
word = text.split()
total = sum(len(word) for word in text.split())
avg = total/len(word)
print("The average word length in the text you entered is", avg, ".")
