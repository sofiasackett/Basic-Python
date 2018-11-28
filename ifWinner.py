#program to identify prize winners
initial = input("Enter the first letter of your name: ")
age = int(input("Enter your age: "))
if initial == "B" and age <= 5:
    print ("You are a winner!!")
elif age == 99:
    print ("You are a winner!!")
elif initial == "W" and age ==21:
    print ("You are our favorite winner")
else:
    print("so sorry...")
