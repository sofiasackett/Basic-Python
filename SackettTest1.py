# Sofia Sackett
# This program calculates how many digits are in a number between 1 and 1000
# This program also outputs the last digit of the number entered

# Input
inp = input('Please enter a number between 1 and 1000: ')

# Try/except
try:
    num = int(inp)
except:
    print('Something went wrong. Please enter a valid integer.')

if num >= 1 and num <= 1000:
    # Determine the number of digits in number
    length = len(inp)

    # Determine the last digit entered
    # When dividing a number by 10, the remainder always equals the ones digit
    lastDigit = num % 10

    # Output
    print('There are ' + str(length) + ' digits in your number.')
    print('The last digit of your number is ' + str(lastDigit) + '.')

elif num < 1 or num > 1000:
    print ('Something went wrong. Please enter an integer between 1 and 1000.')



