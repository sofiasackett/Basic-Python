#Calculate weekly pay given hours worked and hourly pay, where OT is time-and-a-haif

#greetings and input hours worked and hourly pay
print("This program will calculate weekly pay...\n")
hours_worked = float(input("Enter hours worked here: "))
hourly_pay = float(input("Enter hourly rate here: "))

#calculate weekly pay
if hours_worked > 40:
    OT = hours_worked - 40
    weekly_pay = (40 * hourly_pay) + (OT * (hourly_pay * 1.5))
else:
    weekly_pay = hours_worked * hourly_pay

#output weekly pay
weekly_pay = round(weekly_pay, 2)
print(weekly_pay)
    
    
