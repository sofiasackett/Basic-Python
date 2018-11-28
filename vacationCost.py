# This program will give the cost per week of a vaction x weeks long
# We will use an input validation loop to ensure that the user gives valid input

#program greetings
print("We will calculate the cost per week of a vacation given the number of weeks...\n")

#input validation
numWeeks = int(1)
while numWeeks < 4 or numWeeks > 16 :
    numWeeks = input("Please enter a positive number of weeks between 4 and 16: ")
    numWeeks = int(numWeeks)
if 16 >=numWeeks >=4:
    if numWeeks >=4 and numWeeks <=6:
        cost = 3080
    elif numWeeks >=7 and numWeeks <=10:
        cost = 2650
    elif numWeeks >=11 and numWeeks <=16:
        cost = 2090

#print cost
print("The cost per week of a", numWeeks, "week long vacation is $", cost, ".")
