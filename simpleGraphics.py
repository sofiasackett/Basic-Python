 #simple graphics programming
from graphics import *
newWin = GraphWin ("Shapes")

#draw a circle
center = Point(100, 100)
redCircle = Circle(center, 30)
redCircle.setFill ("red")
redCircle.draw(newWin)

#draw a line
aLine = Line(Point (20,20), Point (20,100))
aLine.draw(newWin)

#draw a rectangle
aRectangle = Rectangle(Point(100,20), Point(150,100))
aRectangle.draw(newWin)
newWin.getMouse()
newWin.close()
