# Sofia Sackett
# This program calculates the number of letters and vowels in a long word and prints the first five letters

# Create variable and find length of string
word = "floccinaucinihilipilification"
numLetters = str(len(word))
print("The word 'floccinaucinihilipilification' has " + numLetters + " letters.")

# Calculate the first five letters
firstFive = word[:5]
print("The first five letters are " + str(firstFive) + ".")

# Set counts to 0
totalCharacters = 0
numA = 0
numE = 0
numI = 0
numO = 0
numU = 0

# Use a for loop to calculate the number of occurences of each vowel
for letter in word:
    totalCharacters += 1
    if letter == 'a':
        numA +=1
    elif letter == 'e':
        numE +=1
    elif letter == 'i':
        numI +=1
    elif letter == 'o':
        numO +=1
    elif letter == 'u':
        numU +=1
    else:
        pass

# Output vowel occurences
print("Occurences of letter A: " + str(numA))
print("Occurences of letter E: " + str(numE))
print("Occurences of letter I: " + str(numI))
print("Occurences of letter O: " + str(numO))
print("Occurences of letter U: " + str(numU))

