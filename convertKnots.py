#Convert miles per hour to knots (nautical miles per hour)

#input mph
mph = input("Enter miles per hour here: ")
mph = float(mph)

#calculate knots
knots = mph * 1.15078
knots = round(knots, 4)

#print answer
print(mph, "miles per hour is equal to", knots, "nautical miles per hour, or knots.")
