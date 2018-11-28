#find out if a household is eligible for Medicaid

#use try/except/else to ensure valid integer inputs
try:
    children = input("How many children are in the household?")
    children = int(children)
    adults = input("How many adults are in the household?")
    adults = int(adults)
    income = input("What is your monthly income?")
    income = float(income)
except:
    print("ERROR: Only enter numeric values.")
else:
    household = children + adults
    
#find maximum income for a family of 7 or more
    maximum_income = 3689+((household-6)*622)
    if household <3 and children <1 and adults <1 or adults >2:
        print("Unfortunately, you do not qualify for Medicaid at this time.")
        print("In order to receive Medicaid the household applying for coverage must have at least 3 people, with at least 1 child and at least 1 but no more than 2 adults.")   

    else:
        if (household ==3 and income <2981 or
        household ==4 and income <3356 or
        household ==5 and income <3561 or
        household ==6 and income <3689 or
        household >=7 and income < maximum_income):
            print("You are eligible for Medicaid services.")
        else:
            print("You are not eligible for Medicaid services.")
                



    


    
