#this program will draw randomly colored circles or random size  randomly placed in a window

#import random, import graphics, and create graphics window
from random import *
from graphics import *
win = GraphWin("Circles")

#randomly generate colors
def randomcolor():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    return color_rgb(red, green, blue)
    
#randomly generate the circle's center point
def randomcenter():
    x = randint(0, 200)
    y = randint(0, 200)
    return Point(x, y)

#randomly generate the circle's radius
def randomradius():
    return randint(5, 100)

#use for loop to generate 50 circles
def main():
    count = 0
    for i in range(50):
        circle = Circle(randomcenter(), randomradius())
        circle.setFill (randomcolor())
        circle.draw(win)
        count = count + 1
    win.getMouse()
    win.close()
main()
