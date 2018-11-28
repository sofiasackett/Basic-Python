#Determine the distance in km that a surface-to-air missile must travel to reach a given height and angle

#input height and angle
height = input("Enter the height (in km) that the missile reaches here: ")
height = float(height)
angle = input("Enter the angle (in degrees) of the missile's trajectory here: ")
angle = float(angle)

#convert angle measure from degrees to radians
import math
radians = (math.pi/180) * angle

#calculate distance
distance = height/math.sin(radians)
distance = round(distance, 4)

#print distance in km
print("The missile must travel", distance, "km to reach a height of", height, "km at a", angle, "degree angle.")
