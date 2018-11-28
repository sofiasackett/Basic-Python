# Cost per square inch of a pizza

import math

def find_area(num1):
    area = float(math.pi * (num1/2.0)**2)
    return area

def costPerInch(num2, num1):
    cost = (num2) / find_area(num1)
    return cost
    
def main():
    print("This program computes the cost per square inch of a pizza. \n")
    diameter = float(input("Enter the diameter of the pizza (in inches): "))
    price = int(input("Enter the price of the pizza (in cents): "))
    print("\n")
    print("The cost is", int(costPerInch(price, diameter)), "cents per square inch.")

main()



