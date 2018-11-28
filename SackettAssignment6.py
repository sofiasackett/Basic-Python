# Sofia Sackett
# This program randomly generates numbers in range (1,500)
# Outputs the largest number generated and the number of iterations until 500 is generated

import random

# Set the count of iterations and the largest number generated to 0
count = 0
largestNum = 0

# Create a for loop with enough iterations to reach 500
for int in range(0, 5000):
    num = random.randint(1, 500)
    count += 1
    if num > largestNum:
        largestNum = num
        print("The largest integer generated so far is " + str(largestNum) + ".")
    if num == 500:
        print("It took " + str(count) + " iterations to generate the number 500.")
        break

        
        
    
    


