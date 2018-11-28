# GUI program to complement the special date program

from graphics import *
def main():
    win = GraphWin ("Special Date Calculator", 400, 400)
    win.setCoords (0.0, 0.0, 6.0, 6.0)
    win.setBackground("honeydew1")
    
# create title
    title = Text(Point(3,5.5), "Special Date Calculator")
    title.setFace("helvetica")
    title.setSize(24)
    title.setStyle("italic")
    title.setTextColor("purple")
    title.draw(win)

# draw the interface
    Text(Point (2, 4.5), "Enter the month (in numeric form) here: ").draw(win)
    month = Entry (Point (4.5, 4.5), 5)
    month.setText("0")
    month.draw(win)

    Text(Point (2, 4.0), "Enter the day (in numeric form) here: ").draw(win)
    day = Entry (Point (4.5, 4.0), 5)
    day.setText("0")
    day.draw(win)

    Text(Point (2, 3.5), "Enter the year (last two digits) here: ").draw(win)
    year = Entry (Point (4.5, 3.5), 5)
    year.setText("0")
    year.draw(win)

    Text(Point(3, 1.0), "Is this a special date?").draw(win)

    box = Rectangle (Point(2.0, 2.0), Point (4.0, 3.0)).draw(win)
    button  = Text(Point(3, 2.5), "Check!")
    button.draw(win)
    
    output = Text(Point(3, 0.5), "")
    output.draw(win)
    
#wait for mouse click
    win.getMouse()
    
#calculate if inputs yield a special date
    month = eval(month.getText())
    day = eval(day.getText())
    year = eval(year.getText())
    
    if month*day == year:
        output.setText("Yes, it is a special date!")
        button.setText("Quit")
        win.getMouse()
        win.close()
    else:
        output.setText("No, it is not a special date.")
        button.setText("Quit")
        win.getMouse()
        win.close()

main()
