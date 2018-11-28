#this program will generate 50 randomly placed, randomly sized, and randomly colored circles

#import random, graphics, and create graphics window
from random import *
from graphics import *
win = GraphWin("Circles")

#Generate 50 random circles
count = 0
for i in range(50):
    center = Point((randint(5, 150)), (randint(5, 150)))
    radius = randint(5, 100)
    color = color_rgb (randint (0,255), randint (0, 255), randint (0, 255))
    circle = Circle(center, radius)
    circle.setFill(color)
    circle.draw(win)
    count = count + 1

