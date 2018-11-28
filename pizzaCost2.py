#graphics program to calculate cost per square inch of a circular pizza

#import math and graphics, create window
import math 
from graphics import *

def main():
    win = GraphWin ("Pizza Price", 300, 300)
    win.setCoords (0.0, 0.0, 5.0, 5.0)

    #draw the interface inputs
    Text (Point (1.25, 4.2), "Price of pizza:").draw(win)
    pizza_cost = Entry (Point (3.65, 4.2), 5)
    pizza_cost.setText("0.00")
    pizza_cost.draw(win)
    
    Text (Point (1.75, 3.6), "Diameter of pizza (in inches):").draw(win)
    diameter = Entry (Point (3.65, 3.6), 5)
    diameter.setText("0.00")
    diameter.draw(win)

    #draw the calculate button
    box = Rectangle (Point (1.25, 1.9), Point (3.75, 2.9)).draw(win)
    box.setFill("orange")
    box.setOutline("orange")
    button = Text (Point (2.5, 2.35), "Calculate!")
    button.draw(win)

    #draw the interface outputs
    Text (Point (1.5, 1.25), "Cost per square inch:").draw(win)
    Text (Point (1.25, 0.85), "Deal or no deal?").draw(win)
    
    output_costPerInch = Text (Point (3.5, 1.25), "")
    output_costPerInch.draw(win)
    output_decision = Text (Point (3.5, 0.85), "")
    output_decision.draw(win)

    #wait for a mouse click
    win.getMouse()

    #calculate cost
    pizza_cost = eval(pizza_cost.getText())
    diameter = eval(diameter.getText())
    radius = diameter / 2
    area = math.pi * (radius)**2
    costPerInch = pizza_cost / area
    costPerInch = float(costPerInch)

    #make a decision
    if costPerInch > 0.10:
        decision = ("This pizza is too expensive!")
    else:
        decision = ("This is a great deal!")
        
    #display output and change button text
    output_costPerInch.setText("%0.2f" % costPerInch)
    output_decision.setText(decision)
    button.setText("Quit")
    
    #wait for click then quit
    win.getMouse()
    win.close()

main()

