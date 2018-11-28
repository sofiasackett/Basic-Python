# Sofia Sackett
# This program calculates the average number of times that a user checks their phone per hour

# Program greetings 
print("This program will calculate the average number of times that you checked your phone per hour.")
print("To do this, you will need to input the number of hours you were on your phone today,\nas well as how many times you checked your phone in each of those hours.")

# Set initial counters to zero
checksPerHour = 0
counter = 0
totalChecks = 0

# Give the user context for input question
print("Please input the number of times you checked your phone during each of your hours of use,\nbeginning with the first hour.")


# Check for valid input
try:
    hoursUsed = int(input("\nHow many hours were you on your phone today? "))
except:
    print("An error has occured. Please only enter integer values.")
else:

    # Loop to find average number of checks per hour
    while True:    
        try:
            if(counter == hoursUsed):
                break
            else:
                counter += 1
                checksPerHour = input("Enter the number of times you check your phone hour by hour: ")
                checksPerHour = int(checksPerHour)
                totalChecks += checksPerHour
                continue
        except:
            print("An error has occured. Please only enter integer values.")

averageChecks = totalChecks/hoursUsed
print("You checked your phone an average of " + str(averageChecks) + " times today.")
        
            
   

