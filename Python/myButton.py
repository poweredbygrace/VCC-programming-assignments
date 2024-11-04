from Python.graphics import *

class myButton:
    def __init__(self, center, halfWidth, halfHeight, outlineColor, text, win):
        self.center = center
        self.text = text
        self.win = win
        self.label = Text(center, text)
        self.label.draw(win)
        self.rect = Rectangle(Point(center.getX()-halfWidth, center.getY()-halfHeight), Point(center.getX()+halfWidth, center.getY()+halfHeight))
        self.rect.setOutline(outlineColor)
        self.rect.draw(win)

    def isClicked(self, pos):
        p1 = self.rect.getP1()
        p2 = self.rect.getP2()
        # print("P1= ", p1, "; P2= ", p2)

        insideButtonClicked = False
        #while insideButtonClicked == False:
        #clickPosition = win.getMouse()
        # print("clickPosition.getX() >= p1.getX() ? ", clickPosition.getX() >= p1.getX())
        insideButtonClicked = pos.getX() >= p1.getX() and \
                          pos.getX() <= p2.getX() and \
                          pos.getY() >= p1.getY() and \
                          pos.getY() <= p2.getY()
        return insideButtonClicked

    def setText(self, text):
        self.label.setText(text)