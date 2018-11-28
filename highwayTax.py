#This program finds the highway tax given a full market house value

#program greetings and input house value
print("This program finds the highway tax given a full market house value. \n")
house_value = input("Enter a house value here: ")
house_value = float(house_value)

#find the assessed value of a house at 90% of full market value
assessed_value = house_value *0.9

#calculate highway tax where tax = 0.00079 of the assessed value
highway_tax = assessed_value * 0.00079
highway_tax = format(highway_tax, ".2f")

#output highway tax
print("For a house with a full market value of ", house_value, "the highway tax is $", highway_tax)
