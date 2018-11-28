# Sofia Sackett
# This program will sum the following series, 1/100 + 3/100 + 5/100 +... n/100
# The program will terminate when the highest possible total less than one is reached

# Set total and iteration count equal to 0 
total = 0
count = 0

# Set the first numerator equal to -1 so we can add 2 during each iteration
numerator = -1 

# Create a while loop that counts iterations, adds two to each numerator, and calculates total
while total < 1:
    numerator += 2
    total += (numerator/100)
    count += 1

# If the total sums to one after going through the loop, subtract one iteration from total and count
    if total == 1:
        total -= (numerator/100)
        count -= 1
        break
         
# Print output
print("The highest possible sum less than one is: " + str(total) + ".")
print("It took " + str(count) + " iterations to reach the highest sum less than one.")
