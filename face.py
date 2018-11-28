#draw a face with simple graphics shapes

#open graphics window
from graphics import *
win = GraphWin("Face")

#draw a circle for the head
center = Point (100, 100)
head = Circle (center, 50)
head.setFill(color_rgb(255, 239, 213))
head.draw(win)

#draw left eye
left_iris = Circle(Point(80, 85), 15)
left_iris.setFill("green")
left_iris.draw(win)

left_pupil = Circle(Point(80, 85), 5)
left_pupil.setFill("black")
left_pupil.draw(win)

#clone left eye to make right eye and shift over to the right
right_iris = left_iris.clone()
right_iris.move(40, 0)
right_iris.draw(win)

right_pupil = left_pupil.clone()
right_pupil.move(40, 0)
right_pupil.draw(win)

#draw mouth with line segments
mouth = Polygon(Point(80,115), Point(90,130),Point(110, 130), Point(120, 115))
mouth.setFill("red3")
mouth.draw(win)
