#program using coordinate transformation

from graphics import *
def main():
    win = GraphWin ("Tic-Tac-Toe", 500, 500)
    #set coordinates to go from (0, 0) in the lower left corner to (3, 3) in the upper right
    win.setCoords (0.0, 0.0, 5.0, 5.0)

    #draw the vertical lines
    Line (Point (1, 0), Point (1, 5)).draw(win)
    Line (Point (2, 0), Point (2, 5)).draw(win)
    Line (Point (3, 0), Point (3, 5)).draw(win)
    Line (Point (4, 0), Point (4, 5)).draw(win)

    #draw the horizontal lines
    Line (Point (0, 1), Point (5, 1)).draw(win)
    Line (Point (0, 2), Point (5, 2)).draw(win)
    Line (Point (0, 3), Point (5, 3)).draw(win)
    Line (Point (0, 4), Point (5, 4)).draw(win)

    #wait for click then quit
    win.getMouse()
    win.close()

main()
