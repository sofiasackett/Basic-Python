# Sofia Sackett
# This program calculates the percentage of unique words in the first four chapters of A Tale of Two Citites

# Import string, open tale file, and create dictionary
import string
try: 
    fhand = open("tale4653.txt")
except:
    print("The file cannot be opened. The application will now close.")
    exit()

wordCount = dict()
# Use a for loop to split each line and add words to dictionary
for line in fhand:
    line = line.translate(str.maketrans(' ',' ','!"#$%&\()*+,-./:;<=>?@[\\]^_`{|}~')) 
    line = line.lower()
    words = line.split()

    # Add a new wordCount entry for each new word, otherwise increase frequency of word by 1
    for word in words:
        if word not in wordCount:
            wordCount[word] = 1
        else:
            wordCount[word] += 1

fhand.close()


# Create a list to store the wordCount words and keys in alphabetical order
taleList = wordCount.keys()
taleList = sorted(taleList)

# Use another for loop to count the number of unique words
count = 0
for key in taleList:
    if wordCount[key] ==1:
        count += 1
    else:
        pass

# Calculate the percentage of unique words and print labelled output
percentUnique = (count/4653) * 100
percentUnique = round(percentUnique, 3)
print("The percentage of unique words in the first four chapters of A Tale of Two Cities is " + str(percentUnique) + "%.")
    







