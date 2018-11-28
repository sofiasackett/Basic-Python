# This program will write a series of random integers to a file
import random

#ask the user for a file name to write to and how many numbers we should generate
file_name = input("Enter the file name to write to: ")
num_amount = int(input("Enter how many random numbers you would like: "))

output = open(file_name, "w")
for i in range(num_amount):
    random_num = random.randint(1, 250)
    output.write(str(random_num)+ "\n")
output.close()

output = open(file_name, "r")
print("Here is your file:")
print(output.read())

