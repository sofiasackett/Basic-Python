#This program will output the cost of an online coffee order given pounds of coffee purchased

#program greetings and input amount of coffee in pounds
print("We are going to calculate the cost of an order from Uncommon Grounds Coffee Shop. \n")
pounds = input("Enter the amount of coffee purchased in pounds: ")
pounds = float(pounds)

#calculate cost of coffee
coffee_cost = pounds * 12.55
coffee_cost = round(coffee_cost, 2)

#calculate shipping cost
shipping_cost = (pounds * 0.99) + 4.00
shipping_cost = round(shipping_cost, 2)

#calculate total cost and round to nearest hundredth
total_cost = coffee_cost + shipping_cost
total_cost = round(total_cost, 2)

#output total cost
print("\n")
print("The total cost of your order is $", total_cost, "\n")
print("The cost of coffee is $", coffee_cost, "\n")
print("The cost of shipping and handling is $", shipping_cost)


