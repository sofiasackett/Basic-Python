#This program finds the sum of four non-separated single-digit numbers

#program greetings and input
print("We will calculate the sum of the digits in a four-digit number. \n")
four_digit = input("Enter any four digit number here without separation: ")

#set accumulator variable digit_accum = 0
digit_accum = 0

#add each of the four digits together using a for loop
for i in range(4):
    digit_accum = digit_accum + int(four_digit[i])

#print sum
print("The sum of the digits in", four_digit, "is", digit_accum, ".")
