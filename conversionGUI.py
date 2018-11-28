#Program to convert Celsius to Fahrenheit using a simple GUI 

from graphics import *
def main():
    win = GraphWin("Knots Converter", 400, 300)
    win.setCoords (0.0, 0.0, 3.0, 4.0)

#draw the interface
    Text (Point (1, 3), "Miles per Hour: ").draw(win)
    Text (Point (1, 1), "Knots: ").draw(win)
    input = Entry (Point (2, 3), 5)
    input.setText("0.0")
    input.draw(win)
    
    output = Text (Point (2, 1), "")
    output.draw(win)
    button = Text (Point (1.5, 2.0), "Convert It")
    button.draw(win)
    Rectangle (Point (1, 1.5), Point (2, 2.5)).draw(win)

#wait for a mouse click
    win.getMouse()

    #convert input
    mph = eval(input.getText())
    knots = mph * 1.15078

    #display output and change button
    output.setText("%0.1f" % knots)
    button.setText("Quit")

    #wait for click then quit
    win.getMouse()
    win.close()

main()
