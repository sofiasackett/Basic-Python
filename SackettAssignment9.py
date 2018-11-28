# Sofia Sackett
# This program changes a quote to lowercase and tokenizes and prints each word
# This program will also use a for loop to count and print each letter of a word, then capitalize the first letter

# A QUOTE
quote = "Be the change that you wish to see in the world."
lowercaseQuote = quote.lower()
token = lowercaseQuote.split()

count = 0
for word in token:
    count += 1
    print(word)

print("Word count: " + str(count))

# A WORD
word = "contradistinguish"
count = 0

for letter in word:
    count += 1
    print(letter)

print(word.capitalize())

    
