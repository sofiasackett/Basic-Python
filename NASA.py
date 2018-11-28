#this program will print a time only if two or more computers calculated the same number

try:
    first_time = float(input("Enter the time calculated by the first computer: "))
    second_time = float(input("Enter the time calculated by the second computer: "))
    third_time = float(input("Enter the time calculated by the third computer: "))
except:
    print("An error occured: please try again and remember to enter only numeric values.")
else:
    if first_time == second_time:
        print(first_time)
    elif first_time == third_time:
        print(first_time)
    elif second_time == third_time:
        print(second_time)
    elif second_time != third_time != first_time:
        print("Discard all computation: each computer calculated a different time result.")
