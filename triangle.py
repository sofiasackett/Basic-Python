# Interactive graphics program to draw a triangle and calculate the perimeter

import math
from graphics import *

def square (x):
    return x**2

def distance(p1, p2):
    dist = math.sqrt(square(p2.getX() - p1.getX()) + square(p2.getY() - p1.getY()))
    return dist

def triArea(a, b, c):
    s = (a + b + c)/2.0
    return math.sqrt(s*(s-a)*(s-b)*(s-c))
                     
def main():
    win = GraphWin("Draw a Triangle", 500, 500)
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message1 = Text (Point (5, 1), "Click on three points")
    message1.draw(win)
    message2 = Text(Point(5, 0.5), "")
    message2.draw(win)
                     
#get and draw three vertices of triangle
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

#use polygon object to draw the triangle
    triangle = Polygon (p1, p2, p3)
    triangle.setFill ("peachpuff")
    triangle.setOutline ("cyan")
    triangle.draw(win)

#calculate the perimeter of the triangle
    d1 = distance(p1, p2)
    d2 = distance(p2, p3)
    d3 = distance(p3, p1)
    msg1 = "perimeter: " + str(d1 +d2 + d3)
    print(message1)
    msg2 = "area: " + str(triArea(d1, d2, d3))
    message1.setText(msg1)
    message2.setText(msg2)
    
#wait for another click to exit
    win.getMouse()
    win.close()
    
main()
