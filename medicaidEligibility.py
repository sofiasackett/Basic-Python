#This program will determine if a family is eligible for Medicaid based on size and monthly income

#program greetings and input
print("We will calculate whether your child(ren) is/are eligible to receive Medicaid services..\n")

#ensure that the user inputs valid numeric values
try:
    numChild = int(input("Please enter the number of children in your household: "))
    numAdult = int(input("Please enter the number of adults in your household: "))
    income = int(input("Please enter your monthly income:"))
except:
    print("An error has occured. Please only input integer values.")

#ensure that the family size is at least 3, and there is at least 1 but no more than 2 adults
else:
    familySize = numChild + numAdult
    if familySize >= 3 and numAdult>=1 and numAdult<=2 and numChild >=1:

#determine the maximum income cutoff for families of size 3 or more
        if familySize == 3:
            if income < 2981:
                print("Congratulations, you are eligible for Medicaid services.")
            elif income >= 2981:
                print("Sorry, you are ineligible for Medicaid services. A household of three people must have a monthly income less than $2981.")
        elif familySize == 4:
            if income < 3356:
                print("Congratulations, you are eligible for Medicaid services.")
            elif income >= 3356:
                print("Sorry, you are ineligible for Medicaid services. A household of four people must have a monthly income less than $3356.")
        elif familySize == 5:
            if income < 3561:
                print("Congratulations, you are eligible for Medicaid services.")
            elif income >= 3561:
                print("Sorry, you are ineligible for Medicaid services. A household of five people must have a monthly income less than $3561.")
        elif familySize == 6:
            if income < 3689:
                print("Congratulations, you are eligible for Medicaid services.")
            elif income >= 3689:
                print("Sorry, you are ineligible for Medicaid services. A household of six people must have a monthly income less than $3689.")
        elif familySize >= 7:
            if income < ((familySize - 6) * 622) + 3689:
                print("Congratulations, you are eligible for Medicaid services.")
            elif income >= ((familySize -6)* 622) +3689:
                print("Sorry, you are ineligible for Medicaid services. A household of six people must have a monthly income less than $3689.")
    else:
        print("Sorry, you are ineligible for Medicaid services. A household must consist of a")
        print("minimum of three people, with at least one child and one or two adults.")
