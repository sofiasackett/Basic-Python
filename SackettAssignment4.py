# Sofia Sackett
# This program will display a random proverb upon request

# Welcome message and request input
print('Hello, welcome to the random proverb generator!')

# Ensure that the user inputs a valid integer
try:
    num = int(input('Please enter a positive integer and receive a proverb: '))

except:
    print('An error has occured. Please only input positive integer values.')

else:
    print('You have entered ' + str(num) + '.')
    print('\n')

    # Convert the integer
    num = int(num)
    newNum = num % 7

    # Output values
    if newNum == 0:
        print('\"A good mind possesses a kingdom.\"')
        print('This proverb means that intellectual assets can provide great power,\n whereas material goods are fleeting and relatively unimportant.')
    
    elif newNum == 1:
        print('\"Don\'t cut off your nose to spite your face.\"')
        print('This proverb means that you should take care not to spite others in a way that will cause more harm to yourself.')

    elif newNum == 2:
        print('\"The early bird catches the worm. But the second mouse gets the cheese.\"')
        print('This proverb can mean that the pioneer is rewarded, but it also implies \n that the one who comes after him will gain riches from his discovery.')

    elif newNum == 3:
        print('\"An ounce of discretion is worth a pound of wit.\"')
        print('This proverb means that it is often more clever to be cautious and avoid \n sticky situations rather than rely on smarts to get out of them.')

    elif newNum == 4:
        print('\"A rolling stone gathers no moss.\"')
        print('This proverbs means that the person who does not stay in one place cannot accumulate wealth or put down roots.')

    elif newNum == 5:
        print('\"Time and tide wait for none.\"')
        print('This proverb means that if you do not prepare and plan for the future, you will be taken by surprise.')

    elif newNum == 6:
        print('\"Advice most needed is least heeded.\"')
        print('This proverb means that those who are in desperate need of advice are the least likely to take it.')

    elif newNum == 7:
        print('\"A bad workman blames his tools.\"')
        print('This proverb means that only a poor worker would refuse to take responsibility for their mistakes.')

    else:
        print('Sorry, it seems something went wrong. Please try again.')


