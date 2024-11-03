from graphics import *

def rectangle_info():
    win = GraphWin("Rectangle Information", 400, 400)
    win.setBackground("white")

    instruction = Text(Point(200, 20), "Click two opposite corners of a rectangle")
    instruction.draw(win)

    p1 = win.getMouse()
    p2 = win.getMouse()

    rectangle = Rectangle(p1, p2)
    rectangle.setOutline("black")
    rectangle.setFill("lightgray")
    rectangle.draw(win)

    length = abs(p2.getX() - p1.getX())
    width = abs(p2.getY() - p1.getY())
    area = length * width
    perimeter = 2 * (length + width)

    text_info = Text(Point(200, 350), f"Area: {area}, Perimeter: {perimeter}")
    text_info.draw(win)

    win.getMouse() 
    win.close()

if __name__ == "__main__":
    rectangle_info()