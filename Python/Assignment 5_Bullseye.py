from graphics import *

def draw_target():
    win = GraphWin("Bullseye", 400, 400)
    win.setBackground("white")

    center = Point(200, 200)
    radius = 40  
    
    colors = ["yellow", "red", "blue", "black", "white"]

    for i in range(len(colors)-1, -1, -1):
        ring = Circle(center, radius * (i + 1)) 
        ring.setFill(colors[i])
        ring.setOutline(colors[i])
        ring.draw(win)

    win.getMouse()
    win.close()

if __name__ == "__main__":
    draw_target()
