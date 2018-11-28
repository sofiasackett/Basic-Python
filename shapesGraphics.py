#practice graphics program
from graphics import *
newWindow = GraphWin("Shapes")

#draw a cyan square centered at (100, 100)
square = Rectangle (Point(50,50), Point(150, 150))
square.draw(newWindow)
square.setFill("cyan")

#draw three line segments connected to corners of square
line = Line(Point(50, 50), Point (25, 25))
line.draw(newWindow)

line = Line(Point(150, 50), Point (125, 25))
line.draw(newWindow)

line = Line(Point(50, 150), Point (25, 125))
line.draw(newWindow)

#draw two more line segments connecting the box
line = Line(Point(125, 25), Point (25, 25))
line.draw(newWindow)

line = Line(Point(25, 125), Point (25, 25))
line.draw(newWindow)

#add a orange circle to the center of the cyan square
center = Point (100, 100)
circle = Circle(center, 25)
circle.setFill ("orange")
circle.draw(newWindow)
