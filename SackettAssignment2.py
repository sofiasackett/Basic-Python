# Sofia Sackett
# This program calculates the price of chocolates

# Variables
dark = 1.25
milk = .95
white = 1.3
tax = 1.0795

# Input the number of each type of chocolate 
strDark = input("Enter a number of dark chocolate creams: ")
strMilk = input("Enter a number of milk chocolate creams: ")
strWhite = input("Enter a number of white chocolate creams: ")

# Change each input from a string to an integer value
intDark = int(strDark)
intMilk = int(strMilk)
intWhite = int(strWhite)

# Calculate price of each type of chocolate
priceDark = dark * intDark
priceMilk = milk * intMilk
priceWhite = white * intWhite

# Calculate the total price before tax
total = priceDark + priceMilk + priceWhite

# Calculate the final sale price with tax
final_price = total * tax


# Output
print ("The cost of " + strDark + " dark chocolate cream(s), " + strMilk + " milk chocolate cream(s), and " + strWhite + " white chocolate cream(s) is $" + str(final_price))

