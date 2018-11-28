# GUI calculator to accept number of females and males in a class and give percentages of each

from graphics import *

def main():
    win = GraphWin ("Gender Percentage Calculator", 400, 400)
    win.setCoords (0.0, 0.0, 5.0, 5.0)

#draw the interface
    Text (Point (1.15, 3.5), "Number of Females:").draw(win)
    num_females = Entry (Point (3, 3.5), 5)
    num_females.setText("0")
    num_females.draw(win)

    Text (Point (1.15, 4), "Number of Males:").draw(win)
    num_males = Entry (Point (3, 4), 5)
    num_males.setText("0")
    num_males.draw(win)

    Text (Point (1.15, 1.5), "Percentage of Males:").draw(win)
    Text (Point (1.15, 1), "Percentage of Females:").draw(win)
    
    output_females = Text (Point (2.15, 1), "")
    output_females.draw(win)
    output_males = Text (Point (2.15, 1.5), "")
    output_males.draw(win)
    
    button = Text (Point (2.25, 2.5), "Calculate")
    button.draw(win)
    Rectangle (Point (1.25, 2), Point (3.25, 3.)).draw(win)

    #wait for a mouse click
    win.getMouse()

    #calculate percentages
    num_females = eval(num_females.getText())
    num_males = eval(num_males.getText())
    students = num_females + num_males
    percent_females = (num_females/students) * 100
    percent_males = 100 - percent_females
    
    #display output and change button
    output_females.setText("%0.1f" % percent_females)
    output_males.setText("%0.1f" % percent_males)
    button.setText("Quit")

    #wait for click then quit
    win.getMouse()
    win.close()

main()
