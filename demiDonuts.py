# Online ordering for Demi's Donuts

from graphics import *

def main():
    win = GraphWin ("Demi's Donuts Online Ordering", 500, 500)
    win.setCoords (0.0, 0.0, 10.0, 10.0)

# draw the titles
    Text(Point(2, 9), "ITEM").draw(win)
    Text(Point(7, 9), "QUANTITY").draw(win)
    
#draw the coffee inputs
    Text(Point(2.15, 8), "Regular coffee ($1.75):").draw(win)
    regular = Entry(Point (7, 8), 5)
    regular.setText("0")
    regular.draw(win)
    
    Text(Point(2.25, 7.5), "Iced coffee ($2.25): ").draw(win)
    iced = Entry(Point (7, 7.5), 5)
    iced.setText("0")
    iced.draw(win)

    Text(Point(2.25, 7), "Jelly filled donut ($1.30):").draw(win)
    jelly = Entry(Point (7, 7), 5)
    jelly.setText("0")
    jelly.draw(win)
    
    Text(Point(2.25, 6.5), "Cream filled donut ($1.30): ").draw(win)
    cream = Entry(Point (7, 6.5), 5)
    cream.setText("0")
    cream.draw(win)

    Text(Point(2.25, 6), "Traditional plain donut ($0.99):").draw(win)
    plain = Entry(Point (7, 6), 5)
    plain.setText("0")
    plain.draw(win)
    
    Text(Point(2.25, 5.5), "Traditional sugar donut ($0.99): ").draw(win)
    sugar = Entry(Point (7, 5.5), 5)
    sugar.setText("0")
    sugar.draw(win)

    Text(Point(2.25, 5), "Traditional chocolate donut ($0.99): ").draw(win)
    chocolate = Entry(Point (7, 5), 5)
    chocolate.setText("0")
    chocolate.draw(win)

#output and button
    output1 = Text (Point (4.25, 2.9), "")
    output1.draw(win)
    output2 = Text (Point (6.5, 2.9), "")
    output2.draw(win)
    button = Text (Point (5, 3.75), "Order Now")
    button.draw(win)
    Rectangle (Point (4, 3.25), Point (6, 4.25)).draw(win)

#Image
    center = Point (5, 1.5)
    outside = Circle (center, 1)
    outside.setFill("yellow")
    outside.draw(win)

    center = Point(4.65, 1.85)
    left = Circle(center, 0.05)
    left.setFill("black")
    left.draw(win)

    right = left.clone()
    right.move(.65, 0)
    right.draw(win)

    smile = Polygon (Point(4.65, 1.35), Point(4.88, 1.15), Point(5.1, 1.15), Point(5.3, 1.35))
    smile.draw(win)
    
#wait for a mouse click
    win.getMouse()
    
#calculate price
    regular_cost = int(eval(regular.getText())) * 1.75 
    iced_cost = int(eval(iced.getText())) *2.25
    jelly_cost = int(eval(jelly.getText())) * 1.30
    cream_cost = int(eval(cream.getText())) * 1.30
    plain_cost = int(eval(plain.getText())) * 0.99
    sugar_cost = int(eval(sugar.getText())) * 0.99
    chocolate_cost = int(eval(chocolate.getText())) * 0.99

    sum = (regular_cost + iced_cost + jelly_cost + cream_cost
                   +plain_cost + sugar_cost + chocolate_cost)
    sum = round(sum, 2)
    
#display output and change button
    output1.setText("Your order has been placed! You owe: $")
    output2.setText(sum)
    button.setText("Quit")

#wait for click then quit
    win.getMouse()
    win.close()

main()
