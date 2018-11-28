#this program will display a simple cat drawing using the graphics module

#import graphics and display graphics window
from graphics import *
win = GraphWin("Cat")

#draw cat head
head = Oval (Point(20, 30), Point(180, 170))
head.setFill("gray")
head.setOutline("gray")
head.draw(win)

#draw left cat ear
left_ear = Polygon(Point (25,80), Point (15, 15), Point (80, 45))
left_ear.setFill ("gray")
left_ear.setOutline ("gray")
left_ear.draw(win)

#clone left ear for right side
right_ear = Polygon(Point (175,80), Point (185, 15), Point (120, 45))
right_ear.setFill ("gray")
right_ear.setOutline ("gray")
right_ear.draw(win)

#draw left eye
left_iris = Circle(Point (75, 85), 20)
left_iris.setFill("yellow")
left_iris.draw(win)

left_pupil = Circle(Point (85, 85), 5)
left_pupil.setFill("black")
left_pupil.draw(win)

#clone left eye and shift to make right eye
right_iris = left_iris.clone()
right_iris.move(50, 0)
right_iris.draw(win)

right_pupil = left_pupil.clone()
right_pupil.move(50, 0)
right_pupil.draw(win)

#draw cat nose
nose = Polygon(Point (90,115), Point (110, 115), Point (100, 130))
nose.setFill("pink")
nose.setOutline("pink")
nose.draw(win)


