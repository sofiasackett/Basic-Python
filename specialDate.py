# This program will determine whether the user has input a "special date"
# wherein a special date means that the month times the day equals the year

#get date from user
print("Please enter a date... \n")

month = input("Enter the month (in numeric form) here: ")
month = int(month)

day = input("Enter the day (in numeric form) here: ")
day = int(day)

year = input("Enter the two-digit year here: ")
year = int(year)

#define a function to check if the user has entered valid numbers
def checkInput():
    if month <= 12 and month >=0:
        print("")
    else: 
        print("The month you entered is out of the acceptable range. Please try again and enter an integer between 0 and 12.")

    if day <= 31 and day >=0:
        print("")
    else:
        print("The day you entered is out of the acceptable range. Please try again and enter an integer between 0 and 31.")

    if year <= 99 and year >=00:
        print("")
    else:
        print("The year you entered is out of the acceptable range. Please try again and enter a two-digit number between 00 and 99.")
 
#check if inputs are valid and return error if not
checkInput()

#determine if the inputs yield a special date
if month*day == year:
    print(month, "/", day, "/", year, "is a special date!", month, "multiplied by", day, "equals", year, "!")
else:
    print("Sorry, ", month, "/", day, "/", year, "is not a special date.")

