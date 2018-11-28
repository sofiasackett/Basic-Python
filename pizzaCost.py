#accept diameter of pizza and output cost per square inch
diameter = input("Enter the diameter (in inches) of your pizza here: ")
diameter = float(diameter)
cost = input("Enter the cost of your pizza here: ")
cost = float(cost)
radius = diameter/2
radius = float(radius)
pi = 3.14159
area = radius*radius*pi
costperinch = cost/area
print("The cost per square inch of your", diameter, "inch pizza is $", costperinch)

