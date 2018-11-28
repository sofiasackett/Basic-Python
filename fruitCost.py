#accept from the user the number of oranges and lemons and output the amount of money they owe
oranges = input ("Enter number of oranges purchased: ")
oranges = float(oranges)
lemons = input ("Enter number of lemons purchased: ")
lemons = float(lemons)
cost = (oranges*0.30) + (lemons*0.15)
print("The cost of", oranges, "oranges and", lemons, "lemons is $", cost)
