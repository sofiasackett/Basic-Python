#This program will calculate the highway tax given a full market house value using conditionals

#program greetings and input house value
print("This program finds the highway tax given a full market house value. \n")
market_value = input("Enter a house value here: ")
market_value = float(market_value)

#calculate assessed value of the house
if market_value < 300000:
    assessed_value = market_value * 0.9
else:
    assessed_value = market_value * 0.925

#calculate highway tax where tax = 0.00079 of the assessed value
highway_tax = assessed_value * 0.00079
highway_tax = format(highway_tax, ".2f")

#output highway tax
print("For a house with a full market value of $", market_value, "the highway tax is $", highway_tax)
