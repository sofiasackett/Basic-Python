#1. Write a for loop that displays the following numbers: 0, 10, 20, 30, 40, ...1000
count = 0
for num in range(0, 1000, 10):
    print(num)
    count = count + 1
    
#2. Write an input validation loop that asks the user to enter the words "yes" or "no"
answer = "invalid"
while answer != "yes" and answer != "no":
    answer = (input("Please enter 'yes' or 'no': ")).lower()

#3. Write a program that uses nested loops to draw a pattern
col = 0
for row in range(1):
    for col in range (7,0, -1):
        print("", "*" *col)
        col = col + 1
    print()
    
#4. Write a program that accepts a positive nonzero integer from the user,
#then loops to get sum of all integers from 1 to entered number
number = int(input("Enter a positive nonzero integer: "))
if number<=0:
    print("An error has occured. Please enter a positive nonzero integer.")
sum = 0
while number > 0:
    sum = sum + number
    number = number - 1
print(sum)
