# Sofia Sackett
# This program produces a print out of the user's name and calculates an integer based on user input

# Get user input
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
str_integer = input("Please enter a positive integer greater than 10: ")

# Use modulus operator to find the user's significant integer
integer = int(str_integer)
sig_integer = (integer % 9) + 1

#Print the user's name and their significant integer
print(first_name + " " + last_name)
print("This number may figure significantly in your life in the near future: " + str(sig_integer))
