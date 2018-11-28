#Compute the surface area of a cylinder given radius and height in cm

#get inputs from user
radius = input("Enter radius (in centimeters) here: ")
radius = float(radius)
height = input("Enter height (in centimeters) here: ")
height = float(height)

#calculate surface area
pi = float(3.14159)
surface_area = (2*pi*radius**2) + (2*pi*radius)*height

#print surface area
print("The surface area of a cylinder with a radius of", radius, "cm and a height of", height)
print("cm is", surface_area, "square centimeters.")
