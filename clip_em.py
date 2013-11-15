# clip_em.py
# A program that allows multiple users to play an interactive game
#   called Clip 'Em, which is a sort of combination between the games
#   Sorry and Trouble. The game is displayed entirely on a large GUI.

from graphics import *
from random import *
from dieview import DieView
import math

class CButton:

    def __init__(self, win, center, radius, label):
        self.radius = radius
        self.x, self.y = center.getX(), center.getY()
        self.p = Point(self.x, self.y)
        self.circ = Circle(self.p, radius)
        self.circ.setFill("lightgray")
        self.circ.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self, p):
        dist = math.sqrt((self.x - p.getX())**2 + (self.y - p.getY())**2)
        return (self.active and (dist <= self.radius))

    def getLabel(self):
        return self.label.getText()

    def activate(self):
        self.label.setFill("black")
        self.circ.setWidth(2)
        self.active = True

    def deactivate(self):
        self.label.setFill("darkgray")
        self.circ.setWidth(1)
        self.active = False

    def undraw(self):
        self.circ.undraw()
        self.label.undraw()

    def draw(self, win):
        self.circ.draw(win)
        self.label.draw(win)

    def buttonColor(self, color):
        self.circ.setFill(color)

    def textColor(self, color):
        self.label.setFill(color)

    def move(self, win, point):
        x = (point.getX() - self.x)
        y = (point.getY() - self.y)
        self.x = point.getX()
        self.y = point.getY()
        self.circ.move(x,y)
        self.label.move(x,y)


class Button:

    """A button is a labeled rectangle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods.  The clicked(p) method
    returns true if the button is active and p is inside it."""

    def __init__(self, win, center, width, height, label):
        """ Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, 'Quit') """

        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self, p):
        """Returns true if button active and p is inside"""
        return (self.active and
                self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)

    def getLabel(self):
        """Returns the label string of this button."""
        return self.label.getText()

    def activate(self):
        """Sets this button to 'active'."""
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        """Sets this button to 'inactive'."""
        self.label.setFill('darkgray')
        self.rect.setWidth(1)
        self.active = False

    def undraw(self):
        self.rect.undraw()
        self.label.undraw()

    def draw(self, win):
        self.rect.draw(win)
        self.label.draw(win)

    def buttonColor(self, color):
        self.rect.setFill(color)

    def textColor(self, color):
        self.label.setFill(color)


def makeGraphWin():
    win = GraphWin("Clip 'Em", 900, 900)
    win.setCoords(0,0,100,100)
    return win

def printInstructions(win):
    win.setBackground("green4")
    Skip = Button(win, Point(94,4), 9, 5, "SKIP")
    Skip.activate()
    Next = Button(win, Point(50,10), 15, 8, "NEXT")
    Next.activate()
    Next.buttonColor('blue')
    A = Text(Point(50,94),"Clip 'Em")
    A.setSize(36)
    A.setOutline("red")
    A.draw(win)
    B = Text(Point(50,80),"About the Game")
    B.setSize(25)
    B.draw(win)
    C = Text(Point(50,87),"Instructions")
    C.setSize(25)
    a = Text(Point(50,70),"Clip 'Em is a game similar to the games of Trouble or Sorry. Here, four players")
    b = Text(Point(50,60),"choose which color they would like to play as, and they are then represented by")
    c = Text(Point(50,50),"the four markers of their color choice.  The objective of the game is to get ")
    d = Text(Point(50,40),"all four markers to reach the 'Home' triangle at the center of the game board.")
    f = Text(Point(50,20),"Game play proceeds in the following manner:")
    h = Text(Point(50,75),"First, each player enters his or her name in the boxes provided and clicks Next.  Order of play")
    i = Text(Point(50,70),"will be randomly assigned, and players may then choose which color they would like to play as.")
    j = Text(Point(50,65),"Each player rolls one die on their turn.  At the beginning, each player's markers are located")
    k = Text(Point(50,60),"in the Start position. One marker may be moved onto the board when a six is rolled.  This marker")
    l = Text(Point(50,55),"is now in play. During any individual turn, the player will roll the die and click on the marker")
    m = Text(Point(50,50),"they want to move. However, if a marker lands on an occuped space, the previous occupant is")
    n = Text(Point(50,45),"'Clipped' back to their Start position. Only ONE player is allowed to occupy each space. Once a")
    o = Text(Point(50,40),"player is on the board, they proceed counter-clockwise around the board and try to get all")
    p = Text(Point(50,35),"four markers into their Home triangle before the other players do this. The first player to")
    q = Text(Point(50,30),"get all of his or her markers in their respective home wins the game!                    ")
    a.setSize(18)
    b.setSize(18)
    c.setSize(18)
    d.setSize(18)
    f.setSize(18)
    h.setSize(16)
    i.setSize(16)
    j.setSize(16)
    k.setSize(16)
    l.setSize(16)
    m.setSize(16)
    n.setSize(16)
    o.setSize(16)
    p.setSize(16)
    q.setSize(16)
    a.draw(win)
    b.draw(win)
    c.draw(win)
    d.draw(win)
    f.draw(win)
    pt1 = win.getMouse()
    while not (Next.clicked(pt1) or Skip.clicked(pt1)):
        pt1 = win.getMouse()
    if Skip.clicked(pt1):
        Skip.undraw()
        B.undraw()
        a.undraw()
        b.undraw()
        c.undraw()
        d.undraw()
        f.undraw()
    if Next.clicked(pt1):
        Skip.undraw()
        B.undraw()
        a.undraw()
        b.undraw()
        c.undraw()
        d.undraw()
        f.undraw()
        C.draw(win)
        h.draw(win)
        i.draw(win)
        j.draw(win)
        k.draw(win)
        l.draw(win)
        m.draw(win)
        n.draw(win)
        o.draw(win)
        p.draw(win)
        q.draw(win)
        pt2 = win.getMouse()
        while not Next.clicked(pt2):
            pt2 = win.getMouse()
        C.undraw()
        h.undraw()
        i.undraw()
        j.undraw()
        k.undraw()
        l.undraw()
        m.undraw()
        n.undraw()
        o.undraw()
        p.undraw()
        q.undraw()
    Next.undraw()
    A.undraw()

def playerInfo(win):
    Next = Button(win, Point(50,25), 12, 7, "NEXT")
    Next.activate()
    a = Text(Point(50,80), "Enter player names in the boxes provided and click NEXT")
    a.setSize(20)
    a.draw(win)
    b = Entry(Point(50,70), 15)
    b.setText("Player 1")
    b.draw(win)
    c = Entry(Point(50,60), 15)
    c.setText("Player 2")
    c.draw(win)
    d = Entry(Point(50,50), 15)
    d.setText("Player 3")
    d.draw(win)
    e = Entry(Point(50,40), 15)
    e.setText("Player 4")
    e.draw(win)
    pt = win.getMouse()
    while not Next.clicked(pt):
        pt = win.getMouse()
    p1 = b.getText()
    v1 = random()
    p2 = c.getText()
    v2 = random()
    p3 = d.getText()
    v3 = random()
    p4 = e.getText()
    v4 = random()
    a.undraw()
    b.undraw()
    c.undraw()
    d.undraw()
    e.undraw()
    Next.undraw()
    return p1, v1, p2, v2, p3, v3, p4, v4

def playOrder(p1, v1, p2, v2, p3, v3, p4, v4):
    if v1 > v2 and v1 > v3 and v1 > v4:
        Player1 = p1
        if v2 > v3 and v2 > v4:
            Player2 = p2
            if v3 > v4:
                Player3 = p3
                Player4 = p4
            else:
                Player3 = p4
                Player4 = p3
        elif v3 > v2 and v3 > v4:
            Player2 = p3
            if v2 > v4:
                Player3 = p2
                Player4 = p4
            else:
                Player3 = p4
                Player4 = p2
        else:
            Player2 = p4
            if v2 > v3:
                Player3 = p2
                Player4 = p3
            else:
                Player3 = p3
                Player4 = p2
    elif v2 > v1 and v2 > v3 and v2 > v4:
        Player1 = p2
        if v1 > v3 and v1 > v4:
            Player2 = p1
            if v3 > v4:
                Player3 = p3
                Player4 = p4
            else:
                Player3 = p4
                Player4 = p3
        elif v3 > v1 and v3 > v4:
            Player2 = p3
            if v1 > v4:
                Player3 = p1
                Player4 = p4
            else:
                Player3 = p4
                Player4 = p1
        else:
            Player2 = p4
            if v1 > v3:
                Player3 = p1
                Player4 = p3
            else:
                Player3 = p3
                Player4 = p1
    elif v3 > v1 and v3 > v2 and v3 > v4:
        Player1 = p3
        if v1 > v2 and v1 > v4:
            Player2 = p1
            if v2 > v4:
                Player3 = p2
                Player4 = p4
            else:
                Player3 = p4
                Player4 = p2
        elif v2 > v1 and v2 > v4:
            Player2 = p2
            if v1 > v4:
                Player3 = p1
                Player4 = p4
            else:
                Player3 = p4
                Player4 = p1
        else:
            Player2 = p4
            if v1 > v2:
                Player3 = p1
                Player4 = p2
            else:
                Player3 = p2
                Player4 = p1
    else:
        Player1 = p4
        if v1 > v2 and v1 > v3:
            Player2 = p1
            if v2 > v3:
                Player3 = p2
                Player4 = p3
            else:
                Player3 = p3
                Player4 = p2
        elif v2 > v1 and v2 > v3:
            Player2 = p2
            if v1 > v3:
                Player3 = p1
                Player4 = p3
            else:
                Player3 = p3
                Player4 = p1
        else:
            Player2 = p3
            if v1 > v2:
                Player3 = p1
                Player4 = p2
            else:
                Player3 = p2
                Player4 = p1
    return Player1, Player2, Player3, Player4

def playerColors(win, Player1, Player2, Player3, Player4):
    Red = Button(win, Point(20,50),12,12,"")
    White = Button(win, Point(40,50),12,12,"")
    Blue = Button(win, Point(60,50),12,12,"")
    Green = Button(win, Point(80,50),12,12,"")
    Red.buttonColor('red')
    White.buttonColor('white')
    Blue.buttonColor('blue')
    Green.buttonColor('green')
    Red.activate()
    White.activate()
    Blue.activate()
    Green.activate()
    a = Text(Point(50,70), "")
    a.setSize(25)
    a.draw(win)
    person(a, Player1)
    pt = click(win, Red, White, Blue, Green)
    if Red.clicked(pt):
        c1 = picker(Red, "Red")
        person(a, Player2)
        pt = click(win, Red, White, Blue, Green)
        if White.clicked(pt):
            c2 = picker(White, "White")
            person(a, Player3)
            pt = click(win, Red, White, Blue, Green)
            if Blue.clicked(pt):
                c3 = picker(Blue, "Blue")
                c4 = picker(Green, "Green")
            else:
                c3 = picker(Green, "Green")
                c4 = picker(Blue, "Blue")
        elif Blue.clicked(pt):
            c2 = picker(Blue, "Blue")
            person(a, Player3)
            pt = click(win, Red, White, Blue, Green)
            if White.clicked(pt):
                c3 = picker(White, "White")
                c4 = picker(Green, "Green")
            else:
                c3 = picker(Green, "Green")
                c4 = picker(White, "White")
        else:
            c2 = picker(Green, "Green")
            person(a, Player3)
            pt = click(win, Red, White, Blue, Green)
            if White.clicked(pt):
                c3 = picker(White, "White")
                c4 = picker(Blue, "Blue")
            else:
                c3 = picker(Blue, "Blue")
                c4 = picker(White, "White")
    elif White.clicked(pt):
        c1 = picker(White, "White")
        person(a, Player2)
        pt = click(win, Red, White, Blue, Green)
        if Red.clicked(pt):
            c2 = picker(Red, "Red")
            person(a, Player3)
            pt = click(win, Red, White, Blue, Green)
            if Blue.clicked(pt):
                c3 = picker(Blue, "Blue")
                c4 = picker(Green, "Green")
            else:
                c3 = picker(Green, "Green")
                c4 = picker(Blue, "Blue")
        elif Blue.clicked(pt):
            c2 = picker(Blue, "Blue")
            person(a, Player3)
            pt = click(win, Red, White, Blue, Green)
            if Red.clicked(pt):
                c3 = picker(Red, "Red")
                c4 = picker(Green, "Green")
            else:
                c3 = picker(Green, "Green")
                c4 = picker(Red, "Red")
        else:
            c2 = picker(Green, "Green")
            person(a, Player3)
            pt = click(win, Red, White, Blue, Green)
            if Red.clicked(pt):
                c3 = picker(Red, "Red")
                c4 = picker(Blue, "Blue")
            else:
                c3 = picker(Blue, "Blue")
                c4 = picker(Red, "Red")
    elif Blue.clicked(pt):
        c1 = picker(Blue, "Blue")
        person(a, Player2)
        pt = click(win, Red, White, Blue, Green)
        if Red.clicked(pt):
            c2 = picker(Red, "Red")
            person(a, Player3)
            pt = click(win, Red, White, Blue, Green)
            if White.clicked(pt):
                c3 = picker(White, "White")
                c4 = picker(Green, "Green")
            else:
                c3 = picker(Green, "Green")
                c4 = picker(White, "White")
        elif White.clicked(pt):
            c2 = picker(White, "White")
            person(a, Player3)
            pt = click(win, Red, White, Blue, Green)
            if Red.clicked(pt):
                c3 = picker(Red, "Red")
                c4 = picker(Green, "Green")
            else:
                c3 = picker(Green, "Green")
                c4 = picker(Red, "Red")
        else:
            c2 = picker(Green, "Green")
            person(a, Player3)
            pt = click(win, Red, White, Blue, Green)
            if Red.clicked(pt):
                c3 = picker(Red, "Red")
                c4 = picker(White, "White")
            else:
                c3 = picker(White, "White")
                c4 = picker(Red, "Red")
    else:
        c1 = picker(Green, "Green")
        person(a, Player2)
        pt = click(win, Red, White, Blue, Green)
        if Red.clicked(pt):
            c2 = picker(Red, "Red")
            person(a, Player3)
            pt = click(win, Red, White, Blue, Green)
            if White.clicked(pt):
                c3 = picker(White, "White")
                c4 = picker(Blue, "Blue")
            else:
                c3 = picker(Blue, "Blue")
                c4 = picker(White, "White")
        elif White.clicked(pt):
            c2 = picker(White, "White")
            person(a, Player3)
            pt = click(win, Red, White, Blue, Green)
            if Red.clicked(pt):
                c3 = picker(Red, "Red")
                c4 = picker(Blue, "Blue")
            else:
                c3 = picker(Blue, "Blue")
                c4 = picker(Red, "Red")
        else:
            c2 = picker(Blue, "Blue")
            person(a, Player3)
            pt = click(win, Red, White, Blue, Green)
            if Red.clicked(pt):
                c3 = picker(Red, "Red")
                c4 = picker(White, "White")
            else:
                c3 = picker(White, "White")
                c4 = picker(Red, "Red")
    a.undraw()
    return c1, c2, c3, c4

def person(a, player):
    a.setText("{0}: Choose your color.".format(player))

def click(win, Red, White, Blue, Green):
    pt = win.getMouse()
    while not (Red.clicked(pt) or White.clicked(pt) or Blue.clicked(pt) or Green.clicked(pt)):
        pt = win.getMouse()
    return pt

def picker(button, color):
    button.deactivate()
    button.undraw()
    c = color 
    return c

def DrawBoard(win, Player1, Player2, Player3, Player4, c1, c2, c3, c4):
    win.setBackground("lightblue4")
    a = Rectangle(Point(14,57.5), Point(86,42.5))
    a.setOutline("darkgray")
    a.setFill("darkgray")
    a.draw(win)
    b = Rectangle(Point(42.5,86), Point(57.5,14))
    b.setOutline("darkgray")
    b.setFill("darkgray")
    b.draw(win)
    c = Rectangle(Point(7,60), Point(12,40))
    d = Rectangle(Point(40,7), Point(60,12))
    e = Rectangle(Point(88,60), Point(93,40))
    f = Rectangle(Point(40,93), Point(60,88))
    c.setOutline(c1)
    d.setOutline(c2)
    e.setOutline(c3)
    f.setOutline(c4)
    c.setFill(c1)
    d.setFill(c2)
    e.setFill(c3)
    f.setFill(c4)
    c.draw(win)
    d.draw(win)
    e.draw(win)
    f.draw(win)
    g = Rectangle(Point(19,52.5), Point(44,47.5))
    h = Rectangle(Point(56,52.5), Point(81,47.5))
    i = Rectangle(Point(47.5,81), Point(52.5,56))
    j = Rectangle(Point(47.5,44), Point(52.5,19))
    g.setOutline(c1)
    h.setOutline(c3)
    i.setOutline(c4)
    j.setOutline(c2)
    g.setFill(c1)
    h.setFill(c3)
    i.setFill(c4)
    j.setFill(c2)
    g.draw(win)
    h.draw(win)
    i.draw(win)
    j.draw(win)
    k = Rectangle(Point(14,47.5), Point(19,42.5))
    l = Rectangle(Point(52.5,19), Point(57.5,14))
    m = Rectangle(Point(81,57.5), Point(86,52.5))
    n = Rectangle(Point(42.5,86), Point(47.5,81))
    k.setOutline(c1)
    l.setOutline(c2)
    m.setOutline(c3)
    n.setOutline(c4)
    k.setFill(c1)
    l.setFill(c2)
    m.setFill(c3)
    n.setFill(c4)
    k.draw(win)
    l.draw(win)
    m.draw(win)
    n.draw(win)
    o = Polygon(Point(44,56), Point(50,50), Point(44,44))
    p = Polygon(Point(44,44), Point(50,50), Point(56,44))
    q = Polygon(Point(56,44), Point(50,50), Point(56,56))
    r = Polygon(Point(56,56), Point(50,50), Point(44,56))
    o.setOutline(c1)
    p.setOutline(c2)
    q.setOutline(c3)
    r.setOutline(c4)
    o.setFill(c1)
    p.setFill(c2)
    q.setFill(c3)
    r.setFill(c4)
    o.draw(win)
    p.draw(win)
    q.draw(win)
    r.draw(win)
    s = Text(Point(10,63), Player1)
    t = Text(Point(50,4), Player2)
    u = Text(Point(90,63), Player3)
    v = Text(Point(50,96), Player4)
    s.setSize(17)
    t.setSize(17)
    u.setSize(17)
    v.setSize(17)
    s.draw(win)
    t.draw(win)
    u.draw(win)
    v.draw(win)
    w = Text(Point(18,83), "Clip 'Em")
    w.setSize(36)
    w.setOutline("red")
    w.draw(win)
    p1 = Circle(Point(16.5,45), .7)
    p1.setOutline("black")
    p1.setFill("black")
    p1.draw(win)
    p2 = clone(win, p1, 5, 0)
    p3 = clone(win, p1, 10, 0)
    p4 = clone(win, p1, 15, 0)
    p5 = clone(win, p1, 20, 0)
    p6 = clone(win, p1, 25, 0)
    p7 = clone(win, p1, 28.5, -3.5)
    p8 = clone(win, p1, 28.5, -8.5)
    p9 = clone(win, p1, 28.5, -13.5)
    p10 = clone(win, p1, 28.5, -18.5)
    p11 = clone(win, p1, 28.5, -23.5)
    p12 = clone(win, p1, 28.5, -28.5)
    p13 = clone(win, p1, 33.5, -28.5)
    p14 = clone(win, p1, 38.5, -28.5)
    p15 = clone(win, p1, 38.5, -23.5)
    p16 = clone(win, p1, 38.5, -18.5)
    p17 = clone(win, p1, 38.5, -13.5)
    p18 = clone(win, p1, 38.5, -8.5)
    p19 = clone(win, p1, 38.5, -3.5)
    p20 = clone(win, p1, 42, 0)
    p21 = clone(win, p1, 47, 0)
    p22 = clone(win, p1, 52, 0)
    p23 = clone(win, p1, 57, 0)
    p24 = clone(win, p1, 62, 0)
    p25 = clone(win, p1, 67, 0)
    p26 = clone(win, p1, 67, 5)
    p27 = clone(win, p1, 67, 10)
    p28 = clone(win, p1, 62, 10)
    p29 = clone(win, p1, 57, 10)
    p30 = clone(win, p1, 52, 10)
    p31 = clone(win, p1, 47, 10)
    p32 = clone(win, p1, 42, 10)
    p33 = clone(win, p1, 38.5, 13.5)
    p34 = clone(win, p1, 38.5, 18.5)
    p35 = clone(win, p1, 38.5, 23.5)
    p36 = clone(win, p1, 38.5, 28.5)
    p37 = clone(win, p1, 38.5, 33.5)
    p38 = clone(win, p1, 38.5, 38.5)
    p39 = clone(win, p1, 33.5, 38.5)
    p40 = clone(win, p1, 28.5, 38.5)
    p41 = clone(win, p1, 28.5, 33.5)
    p42 = clone(win, p1, 28.5, 28.5)
    p43 = clone(win, p1, 28.5, 23.5)
    p44 = clone(win, p1, 28.5, 18.5)
    p45 = clone(win, p1, 28.5, 13.5)
    p46 = clone(win, p1, 25, 10)
    p47 = clone(win, p1, 20, 10)
    p48 = clone(win, p1, 15, 10)
    p49 = clone(win, p1, 10, 10)
    p50 = clone(win, p1, 5, 10)
    p51 = clone(win, p1, 0, 10)
    p52 = clone(win, p1, 0, 5)
    p53 = clone(win, p1, 5, 5)
    p54 = clone(win, p1, 10, 5)
    p55 = clone(win, p1, 15, 5)
    p56 = clone(win, p1, 20, 5)
    p57 = clone(win, p1, 25, 5)
    p58 = clone(win, p1, 28.5, 5)
    p59 = clone(win, p1, 28.5, 2)
    p60 = clone(win, p1, 31.5, 5)
    p61 = clone(win, p1, 28.5, 8)
    p62 = clone(win, p1, 33.5, -23.5)
    p63 = clone(win, p1, 33.5, -18.5)
    p64 = clone(win, p1, 33.5, -13.5)
    p65 = clone(win, p1, 33.5, -8.5)
    p66 = clone(win, p1, 33.5, -3.5)
    p67 = clone(win, p1, 33.5, 0)
    p68 = clone(win, p1, 36.5, 0)
    p69 = clone(win, p1, 33.5, 3)
    p70 = clone(win, p1, 30.5, 0)
    p71 = clone(win, p1, 62, 5)
    p72 = clone(win, p1, 57, 5)
    p73 = clone(win, p1, 52, 5)
    p74 = clone(win, p1, 47, 5)
    p75 = clone(win, p1, 42, 5)
    p76 = clone(win, p1, 38.5, 5)
    p77 = clone(win, p1, 38.5, 8)
    p78 = clone(win, p1, 35.5, 5)
    p79 = clone(win, p1, 38.5, 2)
    p80 = clone(win, p1, 33.5, 33.5)
    p81 = clone(win, p1, 33.5, 28.5)
    p82 = clone(win, p1, 33.5, 23.5)
    p83 = clone(win, p1, 33.5, 18.5)
    p84 = clone(win, p1, 33.5, 13.5)
    p85 = clone(win, p1, 33.5, 10)
    p86 = clone(win, p1, 36.5, 10)
    p87 = clone(win, p1, 33.5, 7)
    p88 = clone(win, p1, 30.5, 10)
    p89 = clone(win, p1, -7, -2.5)
    p90 = clone(win, p1, -7, 2.5)
    p91 = clone(win, p1, -7, 7.5)
    p92 = clone(win, p1, -7, 12.5)
    p93 = clone(win, p1, 26, -35.5)
    p94 = clone(win, p1, 31, -35.5)
    p95 = clone(win, p1, 36, -35.5)
    p96 = clone(win, p1, 41, -35.5)
    p97 = clone(win, p1, 74, -2.5)
    p98 = clone(win, p1, 74, 2.5)
    p99 = clone(win, p1, 74, 7.5)
    p100 = clone(win, p1, 74, 12.5)
    p101 = clone(win, p1, 26, 45.5)
    p102 = clone(win, p1, 31, 45.5)
    p103 = clone(win, p1, 36, 45.5)
    p104 = clone(win, p1, 41, 45.5)

def clone(win, p1, x, y):
    p = p1.clone()
    p.move(x, y)
    p.draw(win)

def turn(win, player1, player2, player3, player4, m1, m2, m3, m4, m5, m6, m7,
         m8, m9, m10, m11, m12, m13, m14, m15, m16):
    turn = player1
    rolldie = Button(win, Point(80,30), 10, 5, "Roll")
    die = DieView(win, Point(80,15), 7)
    positions1 = [0,0,0,0]
    positions2 = [0,0,0,0]
    positions3 = [0,0,0,0]
    positions4 = [0,0,0,0]
    while not gameOver(positions1, positions2, positions3, positions4):
        marker_move(win, positions1[0], m1)
        if positions1[1] == 0:
            marker_move(win, 1, m2)
        else:
            marker_move(win, positions1[1], m2)
        if positions1[2] == 0:
            marker_move(win, 2, m3)
        else:
            marker_move(win, positions1[2], m3)
        if positions1[3] == 0:
            marker_move(win, 3, m4)
        else:
            marker_move(win, positions1[3], m4)
        if positions2[0] == 0:
            marker_move(win, 4, m5)
        else:
            marker_move(win, positions2[0], m5)
        if positions2[1] == 0:
            marker_move(win, 5, m6)
        else:
            marker_move(win, positions2[1], m6)
        if positions2[2] == 0:
            marker_move(win, 6, m7)
        else:
            marker_move(win, positions2[2], m7)
        if positions2[3] == 0:
            marker_move(win, 7, m8)
        else:
            marker_move(win, positions2[3], m8)
        if positions3[0] == 0:
            marker_move(win, 8, m9)
        else:
            marker_move(win, positions3[0], m9)
        if positions3[1] == 0:
            marker_move(win, 9, m10)
        else:
            marker_move(win, positions3[1], m10)
        if positions3[2] == 0:
            marker_move(win, 10, m11)
        else:
            marker_move(win, positions3[2], m11)
        if positions3[3] == 0:
            marker_move(win, 11, m12)
        else:
            marker_move(win, positions3[3], m12)
        if positions4[0] == 0:
            marker_move(win, 12, m13)
        else:
            marker_move(win, positions4[0], m13)
        if positions4[1] == 0:
            marker_move(win, 13, m14)
        else:
            marker_move(win, positions4[1], m14)
        if positions4[2] == 0:
            marker_move(win, 14, m15)
        else:
            marker_move(win, positions4[2], m15)
        if positions4[3] == 0:
            marker_move(win, 15, m16)
        else:
            marker_move(win, positions4[3], m16)
        notify = Text(Point(82,83), "")
        notify.setSize(20)
        notify.draw(win)
        if turn == player1:
            notify.setText("{0}: Roll the die".format(player1))
            rolldie.activate()
            a = win.getMouse()
            while not rolldie.clicked(a):
                a = win.getMouse()
            rolldie.deactivate()
            value = randrange(1, 7)
            die.setValue(value)
            notify.setText("{0}: Choose your marker".format(player1))
            positions1, positions2, positions3, positions4 = moves(win, value, positions1, "player1", m1,
                                                                   m2, m3, m4, m5, m6, m7, m8, m9, m10, m11,
                                                                   m12, m13, m14, m15, m16, positions2,
                                                                   positions3, positions4)
            notify.setText("")
            turn = player2
        elif turn == player2:
            notify.setText("{0}: Roll the die".format(player2))
            rolldie.activate()
            a = win.getMouse()
            while not rolldie.clicked(a):
                a = win.getMouse()
            rolldie.deactivate()
            value = randrange(1, 7)
            die.setValue(value)
            notify.setText("{0}: Choose your marker".format(player2))
            positions2, positions1, positions3, positions4 = moves(win, value, positions2, "player2", m1,
                                                                   m2, m3, m4, m5, m6, m7, m8, m9, m10, m11,
                                                                   m12, m13, m14, m15, m16, positions1,
                                                                   positions3, positions4)
            notify.setText("")
            turn = player3
        elif turn == player3:
            notify.setText("{0}: Roll the die".format(player3))
            rolldie.activate()
            a = win.getMouse()
            while not rolldie.clicked(a):
                a = win.getMouse()
            rolldie.deactivate()
            value = randrange(1, 7)
            die.setValue(value)
            notify.setText("{0}: Choose your marker".format(player3))
            positions3, positions1, positions2, positions4 = moves(win, value, positions3, "player3", m1,
                                                                   m2, m3, m4, m5, m6, m7, m8, m9, m10,
                                                                   m11, m12, m13, m14, m15, m16, positions1,
                                                                   positions2, positions4)
            notify.setText("")
            turn = player4
        else:
            notify.setText("{0}: Roll the die".format(player4))
            rolldie.activate()
            a = win.getMouse()
            while not rolldie.clicked(a):
                a = win.getMouse()
            rolldie.deactivate()
            value = randrange(1, 7)
            die.setValue(value)
            notify.setText("{0}: Choose your marker".format(player4))
            positions4, positions1, positions2, positions3 = moves(win, value, positions4, "player4", m1, m2,
                                                                   m3, m4, m5, m6, m7, m8, m9, m10, m11, m12,
                                                                   m13, m14, m15, m16, positions1, positions2,
                                                                   positions3)
            notify.setText("")
            turn = player1
            
    return positions1, positions2, positions3, positions4

def gameOver(p1, p2, p3, p4):
    return p1 == [73,74,75,76] or p2 == [82,83,84,85] or p3 == [91,92,93,94] or p4 == [100,101,102,103]

def clipped(win, updatedpos, player, positions1, positions2, positions3):
    list = [positions1, positions2, positions3]
    for i in list:
        for p in i:
            if p == updatedpos:
                positions1, positions2, positions3 = check(win, updatedpos, player,
                                                           positions1, positions2,
                                                           positions3)
    return positions1, positions2, positions3

def check(win, updatedpos, player, positions1, positions2, positions3):
    list = [positions1, positions2, positions3]
    l = -1
    for i in list:
        l = l + 1
        n = -1
        for p in i:
            n = n + 1
            if p == updatedpos:
                spot = n
                person = l
                break
    if player == "player1":
        if person == 0:
            if spot == 0:
                positions1[0] = 0
            elif spot == 1:
                positions1[1] = 0
            elif spot == 2:
                positions1[2] = 0
            elif spot == 3:
                positions1[3] = 0
        elif person == 1:
            if spot == 0:
                positions2[0] = 0
            elif spot == 1:
                positions2[1] = 0
            elif spot == 2:
                positions2[2] = 0
            elif spot == 3:
                positions2[3] = 0
        else:
            if spot == 0:
                positions3[0] = 0
            elif spot == 1:
                positions3[1] = 0
            elif spot == 2:
                positions3[2] = 0
            elif spot == 3:
                positions3[3] = 0
    elif player == "player2":
        if person == 0:
            if spot == 0:
                positions1[0] = 0
            elif spot == 1:
                positions1[1] = 0
            elif spot == 2:
                positions1[2] = 0
            elif spot == 3:
                positions1[3] = 0
        elif person == 1:
            if spot == 0:
                positions2[0] = 0
            elif spot == 1:
                positions2[1] = 0
            elif spot == 2:
                positions2[2] = 0
            elif spot == 3:
                positions2[3] = 0
        else:
            if spot == 0:
                positions3[0] = 0
            elif spot == 1:
                positions3[1] = 0
            elif spot == 2:
                positions3[2] = 0
            elif spot == 3:
                positions3[3] = 0
    elif player == "player3":
        if person == 0:
            if spot == 0:
                positions1[0] = 0
            elif spot == 1:
                positions1[1] = 0
            elif spot == 2:
                positions1[2] = 0
            elif spot == 3:
                positions1[3] = 0
        elif person == 1:
            if spot == 0:
                positions2[0] = 0
            elif spot == 1:
                positions2[1] = 0
            elif spot == 2:
                positions2[2] = 0
            elif spot == 3:
                positions2[3] = 0
        else:
            if spot == 0:
                positions3[0] = 0
            elif spot == 1:
                positions3[1] = 0
            elif spot == 2:
                positions3[2] = 0
            elif spot == 3:
                positions3[3] = 0
    else:
        if person == 0:
            if spot == 0:
                positions1[0] = 0
            elif spot == 1:
                positions1[1] = 0
            elif spot == 2:
                positions1[2] = 0
            elif spot == 3:
                positions1[3] = 0
        elif person == 1:
            if spot == 0:
                positions2[0] = 0
            elif spot == 1:
                positions2[1] = 0
            elif spot == 2:
                positions2[2] = 0
            elif spot == 3:
                positions2[3] = 0
        else:
            if spot == 0:
                positions3[0] = 0
            elif spot == 1:
                positions3[1] = 0
            elif spot == 2:
                positions3[2] = 0
            elif spot == 3:
                positions3[3] = 0

    return positions1, positions2, positions3

def moves(win, value, positions, player, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12, m13, m14, m15, m16,
          positions1, positions2, positions3):
    w,x,y,z = positions[0], positions[1], positions[2], positions[3]
    if w+x+y+z == 0:
        if player == "player1":
            if value == 6:
                pmoves6_0(win, player, positions, m1, m2, m3, m4, positions1, positions2, positions3)
            else:
                pass
        if player == "player2":
            if value == 6:
                pmoves6_0(win, player, positions, m5, m6, m7, m8, positions1, positions2, positions3)
            else:
                pass
        if player == "player3":
            if value == 6:
                pmoves6_0(win, player, positions, m9, m10, m11, m12, positions1, positions2, positions3)
            else:
                pass
        if player == "player4":
            if value == 6:
                pmoves6_0(win, player, positions, m13, m14, m15, m16, positions1, positions2, positions3)
            else:
                pass
    elif (w!=0 and x!=0 and y!=0 and z!=0):
        if player == "player1":
            p0zhelper(win, player, positions, value, w, x, y, z, m1, m2, m3, m4,
                      73, 74, 75, 76, positions1, positions2, positions3)
        if player == "player2":
            p0zhelper(win, player, positions, value, w, x, y, z, m5, m6, m7, m8,
                      82, 83, 84, 85, positions1, positions2, positions3)
        if player == "player3":
            p0zhelper(win, player, positions, value, w, x, y, z, m9, m10, m11, m12,
                      91, 92, 93, 94, positions1, positions2, positions3)
        if player == "player4":
            p0zhelper(win, player, positions, value, w, x, y, z, m13, m14, m15, m16,
                      100, 101, 102, 103, positions1, positions2, positions3)
    elif w+x+y == 0:
        if player == "player1":
            p3zhelper(win, player, positions, value, m1, m2, m3, m4, z, 16, 76, 0, 1, 2, 3, positions1, positions2, positions3)
        if player == "player2":
            p3zhelper(win, player, positions, value, m5, m6, m7, m8, z, 29, 85, 0, 1, 2, 3, positions1, positions2, positions3)
        if player == "player3":
            p3zhelper(win, player, positions, value, m9, m10, m11, m12, z, 42, 94, 0, 1, 2, 3, positions1, positions2, positions3)
        if player == "player4":
            p3zhelper(win, player, positions, value, m13, m14, m15, m16, z, 55, 103, 0, 1, 2, 3, positions1, positions2, positions3)
    elif w+x+z == 0:
        if player == "player1":
            p3zhelper(win, player, positions, value, m1, m2, m4, m3, y, 16, 75, 0, 1, 3, 2, positions1, positions2, positions3)
        if player == "player2":
            p3zhelper(win, player, positions, value, m5, m6, m8, m7, y, 29, 84, 0, 1, 3, 2, positions1, positions2, positions3)
        if player == "player3":
            p3zhelper(win, player, positions, value, m9, m10, m12, m11, y, 42, 93, 0, 1, 3, 2, positions1, positions2, positions3)
        if player == "player4":
            p3zhelper(win, player, positions, value, m13, m14, m16, m15, y, 55, 102, 0, 1, 3, 2, positions1, positions2, positions3)
    elif w+y+z == 0:
        if player == "player1":
            p3zhelper(win, player, positions, value, m1, m3, m4, m2, x, 16, 74, 0, 2, 3, 1, positions1, positions2, positions3)
        if player == "player2":
            p3zhelper(win, player, positions, value, m5, m7, m8, m6, x, 29, 83, 0, 2, 3, 1, positions1, positions2, positions3)
        if player == "player3":
            p3zhelper(win, player, positions, value, m9, m11, m12, m10, x, 42, 92, 0, 2, 3, 1, positions1, positions2, positions3)
        if player == "player4":
            p3zhelper(win, player, positions, value, m13, m15, m16, m14, x, 55, 101, 0, 2, 3, 1, positions1, positions2, positions3)
    elif x+y+z == 0:
        if player == "player1":
            p3zhelper(win, player, positions, value, m2, m3, m4, m1, w, 16, 73, 1, 2, 3, 0, positions1, positions2, positions3)
        elif player == "player2":
            p3zhelper(win, player, positions, value, m6, m7, m8, m5, w, 29, 82, 1, 2, 3, 0, positions1, positions2, positions3)
        elif player == "player3":
            p3zhelper(win, player, positions, value, m10, m11, m12, m9, w, 42, 91, 1, 2, 3, 0, positions1, positions2, positions3)
        elif player == "player4":
            p3zhelper(win, player, positions, value, m14, m15, m16, m13, w, 55, 100, 1, 2, 3, 0, positions1, positions2, positions3)
    elif w+x == 0:
        if player == "player1":
            p2zhelper(win, player, positions, value, m1, m2, m3, m4, y, 16, 75, z, 76, 0, 1, 2, 3, positions1, positions2, positions3)
        if player == "player2":
            p2zhelper(win, player, positions, value, m5, m6, m7, m8, y, 29, 84, z, 85, 0, 1, 2, 3, positions1, positions2, positions3)
        if player == "player3":
            p2zhelper(win, player, positions, value, m9, m10, m11, m12, y, 42, 93, z, 94, 0, 1, 2, 3, positions1, positions2, positions3)
        if player == "player4":
            p2zhelper(win, player, positions, value, m13, m14, m15, m16, y, 55, 102, z, 103, 0, 1, 2, 3, positions1, positions2, positions3)
    elif w+y == 0:
        if player == "player1":
            p2zhelper(win, player, positions, value, m1, m3, m2, m4, x, 16, 74, z, 76, 0, 2, 1, 3, positions1, positions2, positions3)
        if player == "player2":
            p2zhelper(win, player, positions, value, m5, m7, m6, m8, x, 29, 83, z, 85, 0, 2, 1, 3, positions1, positions2, positions3)
        if player == "player3":
            p2zhelper(win, player, positions, value, m9, m11, m10, m12, x, 42, 92, z, 94, 0, 2, 1, 3, positions1, positions2, positions3)
        if player == "player4":
            p2zhelper(win, player, positions, value, m13, m15, m14, m16, x, 55, 101, z, 103, 0, 2, 1, 3, positions1, positions2, positions3)
    elif w+z == 0:
        if player == "player1":
            p2zhelper(win, player, positions, value, m1, m4, m2, m3, x, 16, 74, y, 75, 0, 3, 1, 2, positions1, positions2, positions3)
        if player == "player2":
            p2zhelper(win, player, positions, value, m5, m8, m6, m7, x, 29, 83, y, 84, 0, 3, 1, 2, positions1, positions2, positions3)
        if player == "player3":
            p2zhelper(win, player, positions, value, m9, m12, m10, m11, x, 42, 92, y, 93, 0, 3, 1, 2, positions1, positions2, positions3)
        if player == "player4":
            p2zhelper(win, player, positions, value, m13, m16, m14, m15, x, 55, 101, y, 102, 0, 3, 1, 2, positions1, positions2, positions3)
    elif x+y == 0:
        if player == "player1":
            p2zhelper(win, player, positions, value, m2, m3, m1, m4, w, 16, 73, z, 76, 1, 2, 0, 3, positions1, positions2, positions3)
        if player == "player2":
            p2zhelper(win, player, positions, value, m6, m7, m5, m8, w, 29, 82, z, 85, 1, 2, 0, 3, positions1, positions2, positions3)
        if player == "player3":
            p2zhelper(win, player, positions, value, m10, m11, m9, m12, w, 42, 91, z, 94, 1, 2, 0, 3, positions1, positions2, positions3)
        if player == "player4":
            p2zhelper(win, player, positions, value, m14, m15, m13, m16, w, 55, 100, z, 103, 1, 2, 0, 3, positions1, positions2, positions3)
    elif x+z == 0:
        if player == "player1":
            p2zhelper(win, player, positions, value, m2, m4, m1, m3, w, 16, 73, y, 75, 1, 3, 0, 2, positions1, positions2, positions3)
        if player == "player2":
            p2zhelper(win, player, positions, value, m6, m8, m5, m7, w, 29, 82, y, 84, 1, 3, 0, 2, positions1, positions2, positions3)
        if player == "player3":
            p2zhelper(win, player, positions, value, m10, m12, m9, m11, w, 42, 91, y, 93, 1, 3, 0, 2, positions1, positions2, positions3)
        if player == "player4":
            p2zhelper(win, player, positions, value, m14, m16, m13, m15, w, 55, 100, y, 102, 1, 3, 0, 2, positions1, positions2, positions3)
    elif y+z == 0:
        if player == "player1":
            p2zhelper(win, player, positions, value, m3, m4, m1, m2, w, 16, 73, x, 74, 2, 3, 0, 1, positions1, positions2, positions3)
        if player == "player2":
            p2zhelper(win, player, positions, value, m7, m8, m5, m6, w, 29, 82, x, 83, 2, 3, 0, 1, positions1, positions2, positions3)
        if player == "player3":
            p2zhelper(win, player, positions, value, m11, m12, m9, m10, w, 42, 91, x, 92, 2, 3, 0, 1, positions1, positions2, positions3)
        if player == "player4":
            p2zhelper(win, player, positions, value, m15, m16, m13, m14, w, 55, 100, x, 101, 2, 3, 0, 1, positions1, positions2, positions3)
    elif w == 0:
        if player == "player1":
            p1zhelper(win, player, positions, value, m1, m2, m3, m4, x, y, z, 0, 1, 2, 3, 16, 74, 75, 76, positions1, positions2, positions3)
        if player == "player2":
            p1zhelper(win, player, positions, value, m5, m6, m7, m8, x, y, z, 0, 1, 2, 3, 29, 83, 84, 85, positions1, positions2, positions3)
        if player == "player3":
            p1zhelper(win, player, positions, value, m9, m10, m11, m12, x, y, z, 0, 1, 2, 3, 42, 92, 93, 94, positions1, positions2, positions3)
        if player == "player4":
            p1zhelper(win, player, positions, value, m13, m14, m15, m16, x, y, z, 0, 1, 2, 3, 55, 101, 102, 103, positions1, positions2, positions3)
    elif x == 0:
        if player == "player1":
            p1zhelper(win, player, positions, value, m2, m1, m3, m4, w, y, z, 1, 0, 2, 3, 16, 73, 75, 76, positions1, positions2, positions3)
        if player == "player2":
            p1zhelper(win, player, positions, value, m6, m5, m7, m8, w, y, z, 1, 0, 2, 3, 29, 82, 84, 85, positions1, positions2, positions3)
        if player == "player3":
            p1zhelper(win, player, positions, value, m10, m9, m11, m12, w, y, z, 1, 0, 2, 3, 42, 91, 93, 94, positions1, positions2, positions3)
        if player == "player4":
            p1zhelper(win, player, positions, value, m14, m13, m15, m16, w, y, z, 1, 0, 2, 3, 55, 100, 102, 103, positions1, positions2, positions3)
    elif y == 0:
        if player == "player1":
            p1zhelper(win, player, positions, value, m3, m1, m2, m4, w, x, z, 2, 0, 1, 3, 16, 73, 74, 76, positions1, positions2, positions3)
        if player == "player2":
            p1zhelper(win, player, positions, value, m7, m5, m6, m8, w, x, z, 2, 0, 1, 3, 29, 82, 83, 85, positions1, positions2, positions3)
        if player == "player3":
            p1zhelper(win, player, positions, value, m11, m9, m10, m12, w, x, z, 2, 0, 1, 3, 42, 91, 92, 94, positions1, positions2, positions3)
        if player == "player4":
            p1zhelper(win, player, positions, value, m15, m13, m14, m16, w, x, z, 2, 0, 1, 3, 55, 100, 101, 103, positions1, positions2, positions3)
    elif z == 0:
        if player == "player1":
            p1zhelper(win, player, positions, value, m4, m1, m2, m3, w, x, y, 3, 0, 1, 2, 16, 73, 74, 75, positions1, positions2, positions3)
        if player == "player2":
            p1zhelper(win, player, positions, value, m8, m5, m6, m7, w, x, y, 3, 0, 1, 2, 29, 82, 83, 84, positions1, positions2, positions3)
        if player == "player3":
            p1zhelper(win, player, positions, value, m12, m9, m10, m11, w, x, y, 3, 0, 1, 2, 42, 91, 92, 93, positions1, positions2, positions3)
        if player == "player4":
            p1zhelper(win, player, positions, value, m16, m13, m14, m15, w, x, y, 3, 0, 1, 2, 55, 100, 101, 102, positions1, positions2, positions3)
                
    return positions, positions1, positions2, positions3

def p3zhelper(win, player, positions, value, m1zero, m2zero, m3zero, m1nozero,
               l_nozero, start_nozero, home_nozero, comp1, comp2, comp3, comp4, positions1, positions2, positions3):
    if l_nozero == start_nozero:
        pmoves1(win, player, positions, value, m1nozero, comp4, positions1, positions2, positions3)
    elif l_nozero == home_nozero:
        if value == 6:
            psmoves3(win, player, positions, m1zero, m2zero, m3zero, comp1, comp2,
                     comp3, positions1, positions2, positions3)
        else:
            pass
    else:
        if value == 6:
            pmoves6_1(win, player, positions, m1zero, m2zero, m3zero, m1nozero,
                      comp1, comp2, comp3, comp4, positions1, positions2, positions3)
        else:
            pmoves1(win, player, positions, value, m1nozero, comp4, positions1, positions2, positions3) 

def p2zhelper(win, player, positions, value, m1zero, m2zero, m1nozero, m2nozero,
              l1_nozero, start, home1_nozero, l2_nozero, home2_nozero, comp1,
              comp2, comp3, comp4, positions1, positions2, positions3):
    if l1_nozero == start or l2_nozero == start:
        if (l1_nozero + value) == l2_nozero:
            pmoves1(win, player, positions, value, m2nozero, comp4, positions1, positions2, positions3)
        elif (l2_nozero + value) == l1_nozero:
            pmoves1(win, player, positions, value, m1nozero, comp3, positions1, positions2, positions3)
        else:
            pmoves2(win, player, positions, value, m1nozero, m2nozero, comp3,
                    comp4, positions1, positions2, positions3)
    elif l1_nozero == start and l2_nozero == home2_nozero:
        pmoves1(win, player, positions, value, m1nozero, comp3, positions1, positions2, positions3)
    elif l2_nozero == start and l1_nozero == home1_nozero:
        pmoves1(win, player, positions, value, m2nozero, comp4, positions1, positions2, positions3)
    elif l1_nozero == home1_nozero and l2_nozero == home2_nozero:
        if value == 6:
            psmoves2(win, player, positions, m1zero, m2zero, comp1, comp2, positions1, positions2, positions3)
        else:
            pass
    elif l1_nozero == start:
        if (l1_nozero + value) == l2_nozero:
            pmoves1(win, player, positions, value, m2nozero, comp4, positions1, positions2, positions3)
        else:
            pmoves2(win, player, positions, value, m1nozero, m2nozero, comp3,
                    comp4, positions1, positions2, positions3)
    elif l2_nozero == start:
        if (l2_nozero + value) == l1_nozero:
            pmoves1(win, player, positions, value, m1nozero, comp3, positions1, positions2, positions3)
        else:
            pmoves2(win, player, positions, value, m1nozero, m2nozero, comp3,
                    comp4, positions1, positions2, positions3)
    elif l2_nozero == home2_nozero:
        if value == 6:
            psmoves2_1(win, player, positions, value, m1zero, m2zero, m1nozero,
                       comp1, comp2, comp3, positions1, positions2, positions3)
        else:
            pmoves1(win, player, positions, value, m1nozero, comp3, positions1, positions2, positions3)
    elif l1_nozero == home1_nozero:
        if value == 6:
            psmoves2_1(win, player, positions, value, m1zero, m2zero, m2nozero,
                       comp1, comp2, comp4, positions1, positions2, positions3)
        else:
            pmoves1(win, player, positions, value, m2nozero, comp4, positions1, positions2, positions3)
    else:
        if (l1_nozero + value) == l2_nozero:
            if value == 6:
                psmoves2_1(win, player, positions, value, m1zero, m2zero, m2nozero,
                           comp1, comp2, comp4, positions1, positions2, positions3)
            else:
                pmoves1(win, player, positions, value, m2nozero, comp4, positions1, positions2, positions3)
        elif (l2_nozero + value) == l1_nozero:
            if value == 6:
                psmoves2_1(win, player, positions, value, m1zero, m2zero, m1nozero,
                           comp1, comp2, comp3, positions1, positions2, positions3)
            else:
                pmoves1(win, player, positions, value, m1nozero, comp3, positions1, positions2, positions3)
        else:
            if value == 6:
                psmoves2_2(win, player, positions, value, m1zero, m2zero, m1nozero,
                           m2nozero, comp1, comp2, comp3, comp4, positions1, positions2, positions3)
            else:
                pmoves2(win, player, positions, value, m1nozero, m2nozero, comp3,
                        comp4, positions1, positions2, positions3)

def p1zhelper(win, player, positions, value, m1zero, m1nozero, m2nozero, m3nozero,
              l1_nozero, l2_nozero, l3_nozero, comp1, comp2, comp3,
              comp4, start, home1_nozero, home2_nozero, home3_nozero, positions1, positions2, positions3):
    if l1_nozero == home1_nozero and l2_nozero == home2_nozero and l3_nozero == home3_nozero:
        if value == 6:
            psmoves1(win, player, positions, m1zero, comp1, positions1, positions2, positions3)
        else:
            pass
    elif l1_nozero == home1_nozero and l2_nozero == home2_nozero:
        if l3_nozero == start:
            pmoves1(win, player, positions, value, m3nozero, comp4, positions1, positions2, positions3)
        else:
            if value == 6:
                psmoves1_1(win, player, positions, value, m1zero, m3nozero, comp1, comp4, positions1, positions2, positions3)
            else:
                pmoves1(win, player, positions, value, m3nozero, comp4, positions1, positions2, positions3)
    elif l1_nozero == home1_nozero and l3_nozero == home3_nozero:
        if l2_nozero == start:
            pmoves1(win, player, positions, value, m2nozero, comp3, positions1, positions2, positions3)
        else:
            if value == 6:
                psmoves1_1(win, player, positions, value, m1zero, m2nozero, comp1, comp3, positions1, positions2, positions3)
            else:
                pmoves1(win, player, positions, value, m2nozero, comp3, positions1, positions2, positions3)
    elif l2_nozero == home2_nozero and l3_nozero == home3_nozero:
        if l1_nozero == start:
            pmoves1(win, player, positions, value, m1nozero, comp2, positions1, positions2, positions3)
        else:
            if value == 6:
                psmoves1_1(win, player, positions, value, m1zero, m1nozero, comp1, comp2, positions1, positions2, positions3)
            else:
                pmoves1(win, player, positions, value, m1nozero, comp2, positions1, positions2, positions3)
    elif l1_nozero == home1_nozero:
        if l2_nozero == start or l3_nozero == start:
            if (l2_nozero + value) == l3_nozero:
                pmoves1(win, player, positions, value, m3nozero, comp4, positions1, positions2, positions3)
            elif (l3_nozero + value) == l2_nozero:
                pmoves1(win, player, positions, value, m2nozero, comp3, positions1, positions2, positions3)
            else:
                pmoves2(win, player, positions, value, m2nozero, m3nozero, comp3, comp4, positions1, positions2, positions3)
        else:
            if (l2_nozero + value) == l3_nozero:
                if value == 6:
                    psmoves1_1(win, player, positions, value, m1zero, m3nozero, comp1, comp4, positions1, positions2, positions3)
                else:
                    pmoves1(win, player, positions, value, m3nozero, comp4, positions1, positions2, positions3)
            elif (l3_nozero + value) == l2_nozero:
                if value == 6:
                    psmoves1_1(win, player, positions, value, m1zero, m2nozero, comp1, comp3, positions1, positions2, positions3)
                else:
                    pmoves1(win, player, positions, value, m2nozero, comp3, positions1, positions2, positions3)
            else:
                psmoves1_2(win, player, positions, value, m1zero, m2nozero, m3nozero, comp1, comp3, comp4, positions1, positions2, positions3)
    elif l2_nozero == home2_nozero:
        if l1_nozero == start or l3_nozero == start:
            if (l1_nozero + value) == l3_nozero:
                pmoves1(win, player, positions, value, m3nozero, comp4, positions1, positions2, positions3)
            elif (l3_nozero + value) == l1_nozero:
                pmoves1(win, player, positions, value, m1nozero, comp2, positions1, positions2, positions3)
            else:
                pmoves2(win, player, positions, value, m1nozero, m3nozero, comp2, comp4, positions1, positions2, positions3)
        else:
            if (l1_nozero + value) == l3_nozero:
                if value == 6:
                    psmoves1_1(win, player, positions, value, m1zero, m3nozero, comp1, comp4, positions1, positions2, positions3)
                else:
                    pmoves1(win, player, positions, value, m3nozero, comp4, positions1, positions2, positions3)
            elif (l3_nozero + value) == l1_nozero:
                if value == 6:
                    psmoves1_1(win, player, positions, value, m1zero, m1nozero, comp1, comp2, positions1, positions2, positions3)
                else:
                    pmoves1(win, player, positions, value, m1nozero, comp2, positions1, positions2, positions3)
            else:
                psmoves1_2(win, player, positions, value, m1zero, m1nozero, m3nozero, comp1, comp2, comp4, positions1, positions2, positions3)
    elif l3_nozero == home3_nozero:
        if l1_nozero == start or l2_nozero == start:
            if (l1_nozero + value) == l2_nozero:
                pmoves1(win, player, positions, value, m2nozero, comp3, positions1, positions2, positions3)
            elif (l2_nozero + value) == l1_nozero:
                pmoves1(win, player, positions, value, m1nozero, comp2, positions1, positions2, positions3)
            else:
                pmoves2(win, player, positions, value, m1nozero, m2nozero, comp2, comp3, positions1, positions2, positions3)
        else:
            if (l1_nozero + value) == l2_nozero:
                if value == 6:
                    psmoves1_1(win, player, positions, value, m1zero, m2nozero, comp1, comp3, positions1, positions2, positions3)
                else:
                    pmoves1(win, player, positions, value, m2nozero, comp3, positions1, positions2, positions3)
            elif (l2_nozero + value) == l1_nozero:
                if value == 6:
                    psmoves1_1(win, player, positions, value, m1zero, m1nozero, comp1, comp2, positions1, positions2, positions3)
                else:
                    pmoves1(win, player, positions, value, m1nozero, comp2, positions1, positions2, positions3)
            else:
                psmoves1_2(win, player, positions, value, m1zero, m1nozero, m2nozero, comp1, comp2, comp3, positions1, positions2, positions3)
    else:
        if l1_nozero == start or l2_nozero == start or l3_nozero == start:
            if (l1_nozero + value) == l2_nozero or (l1_nozero + value) == l3_nozero:
                if (l2_nozero + value) == l3_nozero:
                    pmoves1(win, player, positions, value, m3nozero, comp4, positions1, positions2, positions3)
                elif (l3_nozero + value) == l2_nozero:
                    pmoves1(win, player, positions, value, m2nozero, comp3, positions1, positions2, positions3)
                else:
                    pmoves2(win, player, positions, value, m2nozero, m3nozero, comp3, comp4, positions1, positions2, positions3)
            elif (l2_nozero + value) == l1_nozero or (l2_nozero + value) == l3_nozero:
                if (l1_nozero + value) == l3_nozero:
                    pmoves1(win, player, positions, value, m3nozero, comp4, positions1, positions2, positions3)
                elif (l3_nozero + value) == l1_nozero:
                    pmoves1(win, player, positions, value, m1nozero, comp2, positions1, positions2, positions3)
                else:
                    pmoves2(win, player, positions, value, m1nozero, m3nozero, comp2, comp4, positions1, positions2, positions3)
            elif (l3_nozero + value) == l1_nozero or (l3_nozero + value) == l2_nozero:
                if (l1_nozero + value) == l2_nozero:
                    pmoves1(win, player, positions, value, m2nozero, comp3, positions1, positions2, positions3)
                elif (l2_nozero + value) == l1_nozero:
                    pmoves1(win, player, positions, value, m1nozero, comp2, positions1, positions2, positions3)
                else:
                    pmoves2(win, player, positions, value, m1nozero, m2nozero, comp2, comp3, positions1, positions2, positions3)
            else:
                pmoves3(win, player, positions, value, m1nozero, m2nozero, m3nozero, comp2, comp3, comp4, positions1, positions2, positions3)
        else:
            if (l1_nozero + value) == l2_nozero or (l1_nozero + value) == l3_nozero:
                if (l2_nozero + value) == l3_nozero:
                    if value == 6:
                        psmoves1_1(win, player, positions, value, m1zero, m3nozero, comp1, comp4, positions1, positions2, positions3)
                    else:
                        pmoves1(win, player, positions, value, m3nozero, comp4, positions1, positions2, positions3)
                elif (l3_nozero + value) == l2_nozero:
                    if value == 6:
                        psmoves1_1(win, player, positions, value, m1zero, m2nozero, comp1, comp3, positions1, positions2, positions3)
                    else:
                        pmoves1(win, player, positions, value, m2nozero, comp3, positions1, positions2, positions3)
                else:
                    if value == 6:
                        psmoves1_2(win, player, positions, value, m1zero, m2nozero, m3nozero, comp1, comp3, comp4, positions1, positions2, positions3)
                    else:
                        pmoves2(win, player, positions, value, m2nozero, m3nozero, comp3, comp4, positions1, positions2, positions3)
            elif (l2_nozero + value) == l1_nozero or (l2_nozero + value) == l3_nozero:
                if (l1_nozero + value) == l3_nozero:
                    if value == 6:
                        psmoves1_1(win, player, positions, value, m1zero, m3nozero, comp1, comp4, positions1, positions2, positions3)
                    else:
                        pmoves1(win, player, positions, value, m3nozero, comp4, positions1, positions2, positions3)
                elif (l3_nozero + value) == l1_nozero:
                    if value == 6:
                        psmoves1_1(win, player, positions, value, m1zero, m1nozero, comp1, comp2, positions1, positions2, positions3)
                    else:
                        pmoves1(win, player, positions, value, m1nozero, comp2, positions1, positions2, positions3)
                else:
                    if value == 6:
                        psmoves1_2(win, player, positions, value, m1zero, m1nozero, m3nozero, comp1, comp2, comp4, positions1, positions2, positions3)
                    else:
                        pmoves2(win, player, positions, value, m1nozero, m3nozero, comp2, comp4, positions1, positions2, positions3)
            elif (l3_nozero + value) == l1_nozero or (l3_nozero + value) == l2_nozero:
                if (l1_nozero + value) == l2_nozero:
                    if value == 6:
                        psmoves1_1(win, player, positions, value, m1zero, m2nozero, comp1, comp3, positions1, positions2, positions3)
                    else:
                        pmoves1(win, player, positions, value, m2nozero, comp3, positions1, positions2, positions3)
                elif (l2_nozero + value) == l1_nozero:
                    if value == 6:
                        psmoves1_1(win, player, positions, value, m1zero, m1nozero, comp1, comp2, positions1, positions2, positions3)
                    else:
                        pmoves1(win, player, positions, value, m1nozero, comp2, positions1, positions2, positions3)
                else:
                    if value == 6:
                        psmoves1_2(win, player, positions, value, m1zero, m1nozero, m2nozero, comp1, comp2, comp3, positions1, positions2, positions3)
                    else:
                        pmoves2(win, player, positions, value, m1nozero, m2nozero, comp2, comp3, positions1, positions2, positions3)
            else:
                if value == 6:
                    psmoves1_3(win, player, positions, value, m1zero, m1nozero, m2nozero, m3nozero,
                           comp1, comp2, comp3, comp4, positions1, positions2, positions3)
                else:
                    pmoves3(win, player, positions, value, m1nozero, m2nozero, m3nozero, comp2, comp3, comp4, positions1, positions2, positions3)

def p0zhelper(win, player, positions, value, w, x, y, z, m1, m2, m3, m4, home1,
              home2, home3, home4, positions1, positions2, positions3):
    if w == home1 and x == home2 and y == home3:
        pmoves1(win, player, positions, value, m4, 3, positions1, positions2, positions3)
    elif w == home1 and x == home2 and z == home4:
        pmoves1(win, player, positions, value, m3, 2, positions1, positions2, positions3)
    elif w == home1 and y == home3 and z == home4:
        pmoves1(win, player, positions, value, m2, 1, positions1, positions2, positions3)
    elif x == home2 and y == home3 and z == home4:
        pmoves1(win, player, positions, value, m1, 0, positions1, positions2, positions3)
    elif w == home1 and x == home2:
        if (y + value) == z:
            pmoves1(win, player, positions, value, m4, 3, positions1, positions2, positions3)
        elif (z + value) == y:
            pmoves1(win, player, positions, value, m3, 2, positions1, positions2, positions3)
        else:
            pmoves2(win, player, positions, value, m3, m4, 2, 3, positions1, positions2, positions3)
    elif w == home1 and y == home3:
        if (x + value) == z:
            pmoves1(win, player, positions, value, m4, 3, positions1, positions2, positions3)
        elif (z + value) == x:
            pmoves1(win, player, positions, value, m2, 1, positions1, positions2, positions3)
        else:
            pmoves2(win, player, positions, value, m2, m4, 1, 3, positions1, positions2, positions3)
    elif w == home1 and z == home4:
        if (x + value) == y:
            pmoves1(win, player, positions, value, m3, 2, positions1, positions2, positions3)
        elif (y + value) == x:
            pmoves1(win, player, positions, value, m2, 1, positions1, positions2, positions3)
        else:
            pmoves2(win, player, positions, value, m2, m3, 1, 2, positions1, positions2, positions3)
    elif x == home2 and y == home3:
        if (w + value) == z:
            pmoves1(win, player, positions, value, m4, 3, positions1, positions2, positions3)
        elif (z + value) == w:
            pmoves1(win, player, positions, value, m1, 0, positions1, positions2, positions3)
        else:
            pmoves2(win, player, positions, value, m1, m4, 0, 3, positions1, positions2, positions3)
    elif x == home2 and z == home4:
        if (w + value) == y:
            pmoves1(win, player, positions, value, m3, 2, positions1, positions2, positions3)
        elif (y + value) == w:
            pmoves1(win, player, positions, value, m1, 0, positions1, positions2, positions3)
        else:
            pmoves2(win, player, positions, value, m1, m3, 0, 2, positions1, positions2, positions3)
    elif y == home3 and z == home4:
        if (w + value) == x:
            pmoves1(win, player, positions, value, m2, 1, positions1, positions2, positions3)
        elif (x + value) == w:
            pmoves1(win, player, positions, value, m1, 0, positions1, positions2, positions3)
        else:
            pmoves2(win, player, positions, value, m1, m2, 0, 1, positions1, positions2, positions3)
    elif w == home1:
        if (x + value) == y or (x + value) == z:
            if (y + value) == z:
                pmoves1(win, player, positions, value, m4, 3, positions1, positions2, positions3)
            elif (z + value) == y:
                pmoves1(win, player, positions, value, m3, 2, positions1, positions2, positions3)
            else:
                pmoves2(win, player, positions, value, m3, m4, 2, 3, positions1, positions2, positions3)
        elif (y + value) == x or (y + value) == z:
            if (x + value) == z:
                pmoves1(win, player, positions, value, m4, 3, positions1, positions2, positions3)
            elif (z + value) == x:
                pmoves1(win, player, positions, value, m2, 1, positions1, positions2, positions3)
            else:
                pmoves2(win, player, positions, value, m2, m4, 1, 3, positions1, positions2, positions3)
        elif (z + value) == x or (z + value) == y:
            if (x + value) == y:
                pmoves1(win, player, positions, value, m3, 2, positions1, positions2, positions3)
            elif (y + value) == x:
                pmoves1(win, player, positions, value, m2, 1, positions1, positions2, positions3)
            else:
                pmoves2(win, player, positions, value, m2, m3, 1, 2, positions1, positions2, positions3)
        else:
            pmoves3(win, player, positions, value, m2, m3, m4, 1, 2, 3, positions1, positions2, positions3)
    elif x == home2:
        if (w + value) == y or (w + value) == z:
            if (y + value) == z:
                pmoves1(win, player, positions, value, m4, 3, positions1, positions2, positions3)
            elif (z + value) == y:
                pmoves1(win, player, positions, value, m3, 2, positions1, positions2, positions3)
            else:
                pmoves2(win, player, positions, value, m3, m4, 2, 3, positions1, positions2, positions3)
        elif (y + value) == w or (y + value) == z:
            if (w + value) == z:
                pmoves1(win, player, positions, value, m4, 3, positions1, positions2, positions3)
            elif (z + value) == w:
                pmoves1(win, player, positions, value, m1, 0, positions1, positions2, positions3)
            else:
                pmoves2(win, player, positions, value, m1, m4, 0, 3, positions1, positions2, positions3)
        elif (z + value) == w or (z + value) == y:
            if (w + value) == y:
                pmoves1(win, player, positions, value, m3, 2, positions1, positions2, positions3)
            elif (y + value) == w:
                pmoves1(win, player, positions, value, m1, 0, positions1, positions2, positions3)
            else:
                pmoves2(win, player, positions, value, m1, m3, 0, 2, positions1, positions2, positions3)
        else:
            pmoves3(win, player, positions, value, m1, m3, m4, 0, 2, 3, positions1, positions2, positions3)
    elif y == home3:
        if (w + value) == x or (w + value) == z:
            if (x + value) == z:
                pmoves1(win, player, positions, value, m4, 3, positions1, positions2, positions3)
            elif (z + value) == x:
                pmoves1(win, player, positions, value, m2, 1, positions1, positions2, positions3)
            else:
                pmoves2(win, player, positions, value, m2, m4, 1, 3, positions1, positions2, positions3)
        elif (x + value) == w or (x + value) == z:
            if (w + value) == z:
                pmoves1(win, player, positions, value, m4, 3, positions1, positions2, positions3)
            elif (z + value) == w:
                pmoves1(win, player, positions, value, m1, 0, positions1, positions2, positions3)
            else:
                pmoves2(win, player, positions, value, m1, m4, 0, 3, positions1, positions2, positions3)
        elif (z + value) == w or (z + value) == x:
            if (w + value) == x:
                pmoves1(win, player, positions, value, m2, 1, positions1, positions2, positions3)
            elif (x + value) == w:
                pmoves1(win, player, positions, value, m1, 0, positions1, positions2, positions3)
            else:
                pmoves2(win, player, positions, value, m1, m2, 0, 1, positions1, positions2, positions3)
        else:
            pmoves3(win, player, positions, value, m1, m2, m4, 0, 1, 3, positions1, positions2, positions3)
    elif z == home4:
        if (w + value) == x or (w + value) == y:
            if (x + value) == y:
                pmoves1(win, player, positions, value, m3, 2, positions1, positions2, positions3)
            elif (y + value) == x:
                pmoves1(win, player, positions, value, m2, 1, positions1, positions2, positions3)
            else:
                pmoves2(win, player, positions, value, m2, m3, 1, 2, positions1, positions2, positions3)
        elif (x + value) == w or (x + value) == y:
            if (w + value) == y:
                pmoves1(win, player, positions, value, m3, 2, positions1, positions2, positions3)
            elif (y + value) == w:
                pmoves1(win, player, positions, value, m1, 0, positions1, positions2, positions3)
            else:
                pmoves2(win, player, positions, value, m1, m3, 0, 2, positions1, positions2, positions3)
        elif (y + value) == w or (y + value) == x:
            if (w + value) == x:
                pmoves1(win, player, positions, value, m2, 1, positions1, positions2, positions3)
            elif (x + value) == w:
                pmoves1(win, player, positions, value, m1, 0, positions1, positions2, positions3)
            else:
                pmoves2(win, player, positions, value, m1, m2, 0, 1, positions1, positions2, positions3)
        else:
            pmoves3(win, player, positions, value, m1, m2, m3, 0, 1, 2, positions1, positions2, positions3)
    else:
        if (w + value) == x or (w + value) == y or (w + value) == z:
            if (x + value) == y or (x + value) == z:
                if (y + value) == z:
                    pmoves1(win, player, positions, value, m4, 3, positions1, positions2, positions3)
                elif (z + value) == y:
                    pmoves1(win, player, positions, value, m3, 2, positions1, positions2, positions3)
                else:
                    pmoves2(win, player, positions, value, m3, m4, 2, 3, positions1, positions2, positions3)
            elif (y + value) == x or (y + value) == z:
                if (x + value) == z:
                    pmoves1(win, player, positions, value, m4, 3, positions1, positions2, positions3)
                elif (z + value) == x:
                    pmoves1(win, player, positions, value, m2, 1, positions1, positions2, positions3)
                else:
                    pmoves2(win, player, positions, value, m2, m4, 1, 3, positions1, positions2, positions3)
            elif (z + value) == x or (z + value) == y:
                if (x + value) == y:
                    pmoves1(win, player, positions, value, m3, 2, positions1, positions2, positions3)
                elif (y + value) ==  x:
                    pmoves1(win, player, positions, value, m2, 1, positions1, positions2, positions3)
                else:
                    pmoves2(win, player, positions, value, m2, m3, 1, 2, positions1, positions2, positions3)
            else:
                pmoves3(win, player, positions, value, m2, m3, m4, 1, 2, 3, positions1, positions2, positions3)
        elif (x + value) == w or (x + value) == y or (x + value) == z:
            if (w + value) == y or (w + value) == z:
                if (y + value) == z:
                    pmoves1(win, player, positions, value, m4, 3, positions1, positions2, positions3)
                elif (z + value) == y:
                    pmoves1(win, player, positions, value, m3, 2, positions1, positions2, positions3)
                else:
                    pmoves2(win, player, positions, value, m3, m4, 2, 3, positions1, positions2, positions3)
            elif (y + value) == w or (y + value) == z:
                if (w + value) == z:
                    pmoves1(win, player, positions, value, m4, 3, positions1, positions2, positions3)
                elif (z + value) == w:
                    pmoves1(win, player, positions, value, m1, 0, positions1, positions2, positions3)
                else:
                    pmoves2(win, player, positions, value, m1, m4, 0, 3, positions1, positions2, positions3)
            elif (z + value) == w or (z + value) == y:
                if (w + value) == y:
                    pmoves1(win, player, positions, value, m3, 2, positions1, positions2, positions3)
                elif (y + value) == w:
                    pmoves1(win, player, positions, value, m1, 0, positions1, positions2, positions3)
                else:
                    pmoves2(win, player, positions, value, m1, m3, 0, 2, positions1, positions2, positions3)
            else:
                pmoves3(win, player, positions, value, m1, m3, m4, 0, 2, 3, positions1, positions2, positions3)
        elif (y + value) == w or (y + value) == x or (y + value) == z:
            if (w + value) == x or (w + value) == z:
                if (x + value) == z:
                    pmoves1(win, player, positions, value, m4, 3, positions1, positions2, positions3)
                elif (z + value) == x:
                    pmoves1(win, player, positions, value, m2, 1, positions1, positions2, positions3)
                else:
                    pmoves2(win, player, positions, value, m2, m4, 1, 3, positions1, positions2, positions3)
            elif (x + value) == w or (x + value) == z:
                if (w + value) == z:
                    pmoves1(win, player, positions, value, m4, 3, positions1, positions2, positions3)
                elif (z + value) == w:
                    pmoves1(win, player, positions, value, m1, 0, positions1, positions2, positions3)
                else:
                    pmoves2(win, player, positions, value, m1, m4, 0, 3, positions1, positions2, positions3)
            elif (z + value) == w or (z + value) == x:
                if (w + value) == x:
                    pmoves1(win, player, positions, value, m2, 1, positions1, positions2, positions3)
                elif (x + value) == w:
                    pmoves1(win, player, positions, value, m1, 0, positions1, positions2, positions3)
                else:
                    pmoves2(win, player, positions, value, m1, m2, 0, 1, positions1, positions2, positions3)
            else:
                pmoves3(win, player, positions, value, m1, m2, m4, 0, 1, 3, positions1, positions2, positions3)
        elif (z + value) == w or (z + value) == x or (z + value) == y:
            if (w + value) == x or (w + value) == y:
                if (x + value) == y:
                    pmoves1(win, player, positions, value, m3, 2, positions1, positions2, positions3)
                elif (y + value) == x:
                    pmoves1(win, player, positions, value, m2, 1, positions1, positions2, positions3)
                else:
                    pmoves2(win, player, positions, value, m2, m3, 1, 2, positions1, positions2, positions3)
            elif (x + value) == w or (x + value) == y:
                if (w + value) == y:
                    pmoves1(win, player, positions, value, m3, 2, positions1, positions2, positions3)
                elif (y + value) == w:
                    pmoves1(win, player, positions, value, m1, 0, positions1, positions2, positions3)
                else:
                    pmoves2(win, player, positions, value, m1, m3, 0, 2, positions1, positions2, positions3)
            elif (y + value) == w or (y + value) == x:
                if (w + value) == x:
                    pmoves1(win, player, positions, value, m2, 1, positions1, positions2, positions3)
                elif (x + value) == w:
                    pmoves1(win, player, positions, value, m1, 0, positions1, positions2, positions3)
                else:
                    pmoves2(win, player, positions, value, m1, m2, 0, 1, positions1, positions2, positions3)
            else:
                pmoves3(win, player, positions, value, m1, m2, m3, 0, 1, 2, positions1, positions2, positions3)
        else:
            pmoves4(win, player, positions, value, m1, m2, m3, m4, positions1, positions2, positions3)


def psmoves1_1(win, player, positions, value, mstart1, mplay1, component1, component2, positions1, positions2, positions3):
    pt = win.getMouse()
    while not (mstart1.clicked(pt) or mplay1.clicked(pt)):
        pt = win.getMouse()
    if player == "player1":
        psmoves1_1helper(win, pt, player, positions, value, mstart1, mplay1,
                         component1, component2, 73, 16, 68, positions1, positions2, positions3)
    elif player == "player2":
        psmoves1_1helper(win, pt, player, positions, value, mstart1, mplay1,
                         component1, component2, 82, 29, 77, positions1, positions2, positions3)
    elif player == "player3":
        psmoves1_1helper(win, pt, player, positions, value, mstart1, mplay1,
                         component1, component2, 91, 42, 86, positions1, positions2, positions3)
    elif player == "player4":
        psmoves1_1helper(win, pt, player, positions, value, mstart1, mplay1,
                         component1, component2, 100, 55, 95, positions1, positions2, positions3)

    return positions, positions1, positions2, positions3

def psmoves1_1helper(win, pt, player, positions, value, mstart1, mplay1,
                     component1, component2, homepos, startpos, arrowpos, positions1, positions2, positions3):
    if player == "player1":
        if mstart1.clicked(pt):
            positions[component1] = positions[component1] + startpos
            positions1, positions2, positions3 = clipped(win, positions[component1], player, positions1, positions2, positions3)
            marker_move(win, positions[component1], mstart1)
        else:
            if (positions[component2] + value) <= (homepos - 1):
                positions[component2] = positions[component2] + value
            elif (positions[component2] + value) > (homepos - 1):
                if component2 == 0:
                    positions[component2] = homepos
                elif component2 == 1:
                    positions[component2] = homepos + 1
                elif component2 == 2:
                    positions[component2] = homepos + 2
                elif component2 == 3:
                    positions[component2] = homepos + 3
            positions1, positions2, positions3 = clipped(win, positions[component2], player, positions1, positions2, positions3)
            marker_move(win, positions[component2], mplay1)
    else:
        if mstart1.clicked(pt):
            positions[component1] = positions[component1] + startpos
            positions1, positions2, positions3 = clipped(win, positions[component1], player, positions1, positions2, positions3)
            marker_move(win, positions[component1], mstart1)
        else:
            if ((positions[component2] + value) > 67
                and positions[component2] < 68):
                dif = 67 - positions[component2]
                positions[component2] = 15 + (value-dif)
            elif (positions[component2] < startpos and
                  (positions[component2] + value) > (startpos - 1)):
                dif = startpos - positions[component2]
                if value == 6:
                    if dif == 1:
                        if component2 == 0:
                            positions[component2] = homepos
                        elif component2 == 1:
                            positions[component2] = homepos + 1
                        elif component2 == 2:
                            positions[component2] = homepos + 2
                        elif component2 == 3:
                            positions[component2] = homepos + 3
                    else:
                        positions[component2] = arrowpos + (value-dif)
                else:
                    positions[component2] = arrowpos + (value-dif)
            elif (positions[component2] + value) > (homepos - 1):
                if component2 == 0:
                    positions[component2] = homepos
                elif component2 == 1:
                    positions[component2] = homepos + 1
                elif component2 == 2:
                    positions[component2] = homepos + 2
                elif component2 == 3:
                    positions[component2] = homepos + 3
            else:
                positions[component2] = positions[component2] + value
            positions1, positions2, positions3 = clipped(win, positions[component2], player, positions1, positions2, positions3)
            marker_move(win, positions[component2], mplay1)

def psmoves1_2(win, player, positions, value, mstart1, mplay1, mplay2,
               component1, component2, component3, positions1, positions2, positions3):
    pt = win.getMouse()
    while not (mstart1.clicked(pt) or mplay1.clicked(pt) or mplay2.clicked(pt)):
        pt = win.getMouse()
    if player == "player1":
        psmoves1_2helper(win, pt, player, positions, value, mstart1, mplay1,
                         mplay2, component1, component2, component3, 16, 68, 73, positions1, positions2, positions3)
    elif player == "player2":
        psmoves1_2helper(win, pt, player, positions, value, mstart1, mplay1,
                         mplay2, component1, component2, component3, 29, 77, 82, positions1, positions2, positions3)
    elif player == "player3":
        psmoves1_2helper(win, pt, player, positions, value, mstart1, mplay1,
                         mplay2, component1, component2, component3, 42, 86, 91, positions1, positions2, positions3)
    elif player == "player4":
        psmoves1_2helper(win, pt, player, positions, value, mstart1, mplay1,
                         mplay2, component1, component2, component3, 55, 95, 100, positions1, positions2, positions3)

    return positions, positions1, positions2, positions3

def psmoves1_2helper(win, pt, player, positions, value, mstart1, mplay1,
                     mplay2, component1, component2, component3, startpos,
                     arrowpos, homepos, positions1, positions2, positions3):
    if player == "player1":
        if mstart1.clicked(pt):
            positions[component1] = positions[component1] + startpos
            positions1, positions2, positions3 = clipped(win, positions[component1], player, positions1, positions2, positions3)
            marker_move(win, positions[component1], mstart1)
        elif mplay1.clicked(pt):
            if (positions[component2] + value) <= 72:
                positions[component2] = positions[component2] + value
            elif (positions[component2] + value) > 72:
                if component2 == 0:
                    positions[component2] = 73
                elif component2 == 1:
                    positions[component2] = 74
                elif component2 == 2:
                    positions[component2] = 75
                elif component2 == 3:
                    positions[component2] = 76
            positions1, positions2, positions3 = clipped(win, positions[component2], player, positions1, positions2, positions3)
            marker_move(win, positions[component2], mplay1)
        else:
            if (positions[component3] + value) <= 72:
                positions[component3] = positions[component3] + value
            elif (positions[component3] + value) > 72:
                if component3 == 0:
                    positions[component3] = 73
                elif component3 == 1:
                    positions[component3] = 74
                elif component3 == 2:
                    positions[component3] = 75
                elif component3 == 3:
                    positions[component3] = 76
            positions1, positions2, positions3 = clipped(win, positions[component3], player, positions1, positions2, positions3)
            marker_move(win, positions[component3], mplay2)
    else:
        if mstart1.clicked(pt):
            positions[component1] = positions[component1] + startpos
            positions1, positions2, positions3 = clipped(win, positions[component1], player, positions1, positions2, positions3)
            marker_move(win, positions[component1], mstart1)
        elif mplay1.clicked(pt):
            if (positions[component2] + value) > 67 and positions[component2] < 68:
                dif = 67 - positions[component2]
                positions[component2] = 15 + (value-dif)
            elif positions[component2] < startpos and (positions[component2] + value) > (startpos - 1):
                dif = startpos - positions[component2]
                if value == 6:
                    if dif == 1:
                        if component2 == 0:
                            positions[component2] = homepos
                        elif component2 == 1:
                            positions[component2] = homepos + 1
                        elif component2 == 2:
                            positions[component2] = homepos + 2
                        elif component2 == 3:
                            positions[component2] = homepos + 3
                    else:
                        positions[component2] = arrowpos + (value-dif)
                else:
                    positions[component2] = arrowpos + (value-dif)
            elif (positions[component2] + value) > (homepos - 1):
                if component2 == 0:
                    positions[component2] = homepos
                elif component2 == 1:
                    positions[component2] = homepos + 1
                elif component2 == 2:
                    positions[component2] = homepos + 2
                elif component2 == 3:
                    positions[component2] = homepos + 3
            else:
                positions[component2] = positions[component2] + value
            positions1, positions2, positions3 = clipped(win, positions[component2], player, positions1, positions2, positions3)
            marker_move(win, positions[component2], mplay1)
        else:
            if (positions[component3] + value) > 67 and positions[component3] < 68:
                dif = 67 - positions[component3]
                positions[component3] = 15 + (value-dif)
            elif positions[component3] < startpos and (positions[component3] + value) > (startpos - 1):
                dif = startpos - positions[component3]
                if value == 6:
                    if dif == 1:
                        if component3 == 0:
                            positions[component3] = homepos
                        elif component3 == 1:
                            positions[component3] = homepos + 1
                        elif component3 == 2:
                            positions[component3] = homepos + 2
                        elif component3 == 3:
                            positions[component3] = homepos + 3
                    else:
                        positions[component3] = arrowpos + (value-dif)
                else:
                    positions[component3] = arrowpos + (value-dif)
            elif (positions[component3] + value) > (homepos - 1):
                if component3 == 0:
                    positions[component3] = homepos
                elif component3 == 1:
                    positions[component3] = homepos + 1
                elif component3 == 2:
                    positions[component3] = homepos + 2
                elif component3 == 3:
                    positions[component3] = homepos + 3
            else:
                positions[component3] = positions[component3] + value
            positions1, positions2, positions3 = clipped(win, positions[component3], player, positions1, positions2, positions3)
            marker_move(win, positions[component3], mplay2)

def psmoves1_3(win, player, positions, value, mstart1, mplay1, mplay2, mplay3,
               component1, component2, component3, component4, positions1, positions2, positions3):
    pt = win.getMouse()
    while not (mstart1.clicked(pt) or mplay1.clicked(pt) or mplay2.clicked(pt)
               or mplay3.clicked(pt)):
        pt = win.getMouse()
    if player == "player1":
        psmoves1_3helper(win, pt, player, positions, value, mstart1, mplay1,
                         mplay2, mplay3, component1, component2, component3,
                         component4, 16, 68, 73, positions1, positions2, positions3)
    elif player == "player2":
        psmoves1_3helper(win, pt, player, positions, value, mstart1, mplay1,
                         mplay2, mplay3, component1, component2, component3,
                         component4, 29, 77, 82, positions1, positions2, positions3)
    elif player == "player3":
        psmoves1_3helper(win, pt, player, positions, value, mstart1, mplay1,
                         mplay2, mplay3, component1, component2, component3,
                         component4, 42, 86, 91, positions1, positions2, positions3)
    elif player == "player4":
        psmoves1_3helper(win, pt, player, positions, value, mstart1, mplay1,
                         mplay2, mplay3, component1, component2, component3,
                         component4, 55, 95, 100, positions1, positions2, positions3)

    return positions, positions1, positions2, positions3

def psmoves1_3helper(win, pt, player, positions, value, mstart1, mplay1, mplay2,
                     mplay3, component1, component2, component3, component4,
                     startpos, arrowpos, homepos, positions1, positions2, positions3):
    if player == "player1":
        if mstart1.clicked(pt):
            positions[component1] = positions[component1] + startpos
            positions1, positions2, positions3 = clipped(win, positions[component1], player, positions1, positions2, positions3)
            marker_move(win, positions[component1], mstart1)
        elif mplay1.clicked(pt):
            if (positions[component2] + value) <= 72:
                positions[component2] = positions[component2] + value
            elif (positions[component2] + value) > 72:
                if component2 == 0:
                    positions[component2] = 73
                elif component2 == 1:
                    positions[component2] = 74
                elif component2 == 2:
                    positions[component2] = 75
                elif component2 == 3:
                    positions[component2] = 76
            positions1, positions2, positions3 = clipped(win, positions[component2], player, positions1, positions2, positions3)
            marker_move(win, positions[component2], mplay1)
        elif mplay2.clicked(pt):
            if (positions[component3] + value) <= 72:
                positions[component3] = positions[component3] + value
            elif (positions[component3] + value) > 72:
                if component3 == 0:
                    positions[component3] = 73
                elif component3 == 1:
                    positions[component3] = 74
                elif component3 == 2:
                    positions[component3] = 75
                elif component3 == 3:
                    positions[component3] = 76
            positions1, positions2, positions3 = clipped(win, positions[component3], player, positions1, positions2, positions3)
            marker_move(win, positions[component3], mplay2)
        else:
            if (positions[component4] + value) <= 72:
                positions[component4] = positions[component4] + value
            elif (positions[component4] + value) > 72:
                if component4 == 0:
                    positions[component4] = 73
                elif component4 == 1:
                    positions[component4] = 74
                elif component4 == 2:
                    positions[component4] = 75
                elif component4 == 3:
                    positions[component4] = 76
            positions1, positions2, positions3 = clipped(win, positions[component4], player, positions1, positions2, positions3)
            marker_move(win, positions[component4], mplay3)
    else:
        if mstart1.clicked(pt):
            positions[component1] = positions[component1] + startpos
            positions1, positions2, positions3 = clipped(win, positions[component1], player, positions1, positions2, positions3)
            marker_move(win, positions[component1], mstart1)
        elif mplay1.clicked(pt):
            if (positions[component2] + value) > 67 and positions[component2] < 68:
                dif = 67 - positions[component2]
                positions[component2] = 15 + (value-dif)
            elif positions[component2] < startpos and (positions[component2] + value) > (startpos - 1):
                dif = startpos - positions[component2]
                if value == 6:
                    if dif == 1:
                        if component2 == 0:
                            positions[component2] = homepos
                        elif component2 == 1:
                            positions[component2] = homepos + 1
                        elif component2 == 2:
                            positions[component2] = homepos + 2
                        elif component2 == 3:
                            positions[component2] = homepos + 3
                    else:
                        positions[component2] = arrowpos + (value-dif)
                else:
                    positions[component2] = arrowpos + (value-dif)
            elif (positions[component2] + value) > (homepos - 1):
                if component2 == 0:
                    positions[component2] = homepos
                elif component2 == 1:
                    positions[component2] = homepos + 1
                elif component2 == 2:
                    positions[component2] = homepos + 2
                elif component2 == 3:
                    positions[component2] = homepos + 3
            else:
                positions[component2] = positions[component2] + value
            positions1, positions2, positions3 = clipped(win, positions[component2], player, positions1, positions2, positions3)
            marker_move(win, positions[component2], mplay1)
        elif mplay2.clicked(pt):
            if (positions[component3] + value) > 67 and positions[component3] < 68:
                dif = 67 - positions[component3]
                positions[component3] = 15 + (value-dif)
            elif positions[component3] < startpos and (positions[component3] + value) > (startpos - 1):
                dif = startpos - positions[component3]
                if value == 6:
                    if dif == 1:
                        if component3 == 0:
                            positions[component3] = homepos
                        elif component3 == 1:
                            positions[component3] = homepos + 1
                        elif component3 == 2:
                            positions[component3] = homepos + 2
                        elif component3 == 3:
                            positions[component3] = homepos + 3
                    else:
                        positions[component3] = arrowpos + (value-dif)
                else:
                    positions[component3] = arrowpos + (value-dif)
            elif (positions[component3] + value) > (homepos - 1):
                if component3 == 0:
                    positions[component3] = homepos
                elif component3 == 1:
                    positions[component3] = homepos + 1
                elif component3 == 2:
                    positions[component3] = homepos + 2
                elif component3 == 3:
                    positions[component3] = homepos + 3
            else:
                positions[component3] = positions[component3] + value
            positions1, positions2, positions3 = clipped(win, positions[component3], player, positions1, positions2, positions3)
            marker_move(win, positions[component3], mplay2)
        else:
            if (positions[component4] + value) > 67 and positions[component4] < 68:
                dif = 67 - positions[component4]
                positions[component4] = 15 + (value-dif)
            elif positions[component4] < startpos and (positions[component4] + value) > (startpos - 1):
                dif = startpos - positions[component4]
                if value == 6:
                    if dif == 1:
                        if component4 == 0:
                            positions[component4] = homepos
                        elif component4 == 1:
                            positions[component4] = homepos + 1
                        elif component4 == 2:
                            positions[component4] = homepos + 2
                        elif component4 == 3:
                            positions[component4] = homepos + 3
                    else:
                        positions[component4] = arrowpos + (value-dif)
                else:
                    positions[component4] = arrowpos + (value-dif)
            elif (positions[component4] + value) > (homepos - 1):
                if component4 == 0:
                    positions[component4] = homepos
                elif component4 == 1:
                    positions[component4] = homepos + 1
                elif component4 == 2:
                    positions[component4] = homepos + 2
                elif component4 == 3:
                    positions[component4] = homepos + 3
            else:
                positions[component4] = positions[component4] + value
            positions1, positions2, positions3 = clipped(win, positions[component4], player, positions1, positions2, positions3)
            marker_move(win, positions[component4], mplay3)

def psmoves2_1(win, player, positions, value, mstart1, mstart2, mplay1, component1, component2, component3, positions1, positions2, positions3):
    pt = win.getMouse()
    while not (mstart1.clicked(pt) or mstart2.clicked(pt) or mplay1.clicked(pt)):
        pt = win.getMouse()
    if player == "player1":
        psmoves2_1helper(win, pt, player, positions, value, mstart1, mstart2, mplay1,
                         component1, component2, component3, 16, 68, 73, positions1, positions2, positions3)
    elif player == "player2":
        psmoves2_1helper(win, pt, player, positions, value, mstart1, mstart2, mplay1,
                         component1, component2, component3, 29, 77, 82, positions1, positions2, positions3)
    elif player == "player3":
        psmoves2_1helper(win, pt, player, positions, value, mstart1, mstart2, mplay1,
                         component1, component2, component3, 42, 86, 91, positions1, positions2, positions3)
    elif player == "player4":
        psmoves2_1helper(win, pt, player, positions, value, mstart1, mstart2, mplay1,
                         component1, component2, component3, 55, 95, 100, positions1, positions2, positions3)

    return positions, positions1, positions2, positions3
            

def psmoves2_1helper(win, pt, player, positions, value, mstart1, mstart2, mplay1,
                     component1, component2, component3, startpos, arrowpos,
                     homepos, positions1, positions2, positions3):
    if player == "player1":
        if mstart1.clicked(pt):
            positions[component1] = positions[component1] + startpos
            positions1, positions2, positions3 = clipped(win, positions[component1], player, positions1, positions2, positions3)
            marker_move(win, positions[component1], mstart1)
        if mstart2.clicked(pt):
            positions[component2] = positions[component2] + startpos
            positions1, positions2, positions3 = clipped(win, positions[component2], player, positions1, positions2, positions3)
            marker_move(win, positions[component2], mstart2)
        if mplay1.clicked(pt):
            if (positions[component3] + value) <= (homepos - 1):
                positions[component3] = positions[component3] + value
            elif (positions[component3] + value) > (homepos - 1):
                if component3 == 0:
                    positions[component3] = (homepos)
                elif component3 == 1:
                    positions[component3] = (homepos + 1)
                elif component3 == 2:
                    positions[component3] = (homepos + 2)
                elif component3 == 3:
                    positions[component3] = (homepos + 3)
            positions1, positions2, positions3 = clipped(win, positions[component3], player, positions1, positions2, positions3)
            marker_move(win, positions[component3], mplay1)
    else:
        if mstart1.clicked(pt):
            positions[component1] = positions[component1] + startpos
            positions1, positions2, positions3 = clipped(win, positions[component1], player, positions1, positions2, positions3)
            marker_move(win, positions[component1], mstart1)
        elif mstart2.clicked(pt):
            positions[component2] = positions[component2] + startpos
            positions1, positions2, positions3 = clipped(win, positions[component2], player, positions1, positions2, positions3)
            marker_move(win, positions[component2], mstart2)
        else:
            if (positions[component3] + value) > 67 and positions[component3] < 68:
                dif = 67 - positions[component3]
                positions[component3] = 15 + (value-dif)
            elif positions[component3] < (startpos) and (positions[component3] + value) > (startpos - 1):
                dif = (startpos) - positions[component3]
                if value == 6:
                    if dif == 1:
                        if component3 == 0:
                            positions[component3] = (homepos)
                        elif component3 == 1:
                            positions[component3] = (homepos + 1)
                        elif component3 == 2:
                            positions[component3] = (homepos + 2)
                        elif component3 == 3:
                            positions[component3] = (homepos + 3)
                    else:
                        positions[component3] = arrowpos + (value-dif)
                else:
                    positions[component3] = arrowpos + (value-dif)
            elif (positions[component3] + value) > (homepos - 1):
                if component3 == 0:
                    positions[component3] = homepos
                elif component3 == 1:
                    positions[component3] = homepos + 1
                elif component3 == 2:
                    positions[component3] = homepos + 2
                elif component3 == 3:
                    positions[component3] = homepos + 3
            else:
                positions[component3] = positions[component3] + value
            positions1, positions2, positions3 = clipped(win, positions[component3], player, positions1, positions2, positions3)
            marker_move(win, positions[component3], mplay1)

def psmoves2_2(win, player, positions, value, mstart1, mstart2, mplay1, mplay2, component1, component2,
               component3, component4, positions1, positions2, positions3):
    pt = win.getMouse()
    while not (mstart1.clicked(pt) or mstart2.clicked(pt) or mplay1.clicked(pt) or mplay2.clicked(pt)):
        pt = win.getMouse()
    if player == "player1":
        psmoves2_2helper(win, pt, player, positions, value, mstart1, mstart2, mplay1,
                     mplay2, component1, component2, component3, component4, 16, 68, 73, positions1, positions2, positions3)
    elif player == "player2":
        psmoves2_2helper(win, pt, player, positions, value, mstart1, mstart2, mplay1,
                     mplay2, component1, component2, component3, component4, 29, 77, 82, positions1, positions2, positions3)
    elif player == "player3":
        psmoves2_2helper(win, pt, player, positions, value, mstart1, mstart2, mplay1,
                     mplay2, component1, component2, component3, component4, 42, 86, 91, positions1, positions2, positions3)
    elif player == "player4":
        psmoves2_2helper(win, pt, player, positions, value, mstart1, mstart2, mplay1,
                     mplay2, component1, component2, component3, component4, 55, 95, 100, positions1, positions2, positions3)

    return positions, positions1, positions2, positions3

def psmoves2_2helper(win, pt, player, positions, value, mstart1, mstart2, mplay1,
                     mplay2, component1, component2, component3, component4, startpos, arrowpos,
                     homepos, positions1, positions2, positions3):
    if player == "player1":
        if mstart1.clicked(pt):
            positions[component1] = positions[component1] + startpos
            positions1, positions2, positions3 = clipped(win, positions[component1], player, positions1, positions2, positions3)
            marker_move(win, positions[component1], mstart1)
        elif mstart2.clicked(pt):
            positions[component2] = positions[component2] + startpos
            positions1, positions2, positions3 = clipped(win, positions[component2], player, positions1, positions2, positions3)
            marker_move(win, positions[component2], mstart2)
        elif mplay1.clicked(pt):
            if (positions[component3] + value) <= (homepos - 1):
                positions[component3] = positions[component3] + value
            elif (positions[component3] + value) > (homepos - 1):
                if component3 == 0:
                    positions[component3] = (homepos)
                elif component3 == 1:
                    positions[component3] = (homepos + 1)
                elif component3 == 2:
                    positions[component3] = (homepos + 2)
                elif component3 == 3:
                    positions[component3] = (homepos + 3)
            positions1, positions2, positions3 = clipped(win, positions[component3], player, positions1, positions2, positions3)
            marker_move(win, positions[component3], mplay1)
        else:
            if (positions[component4] + value) <= (homepos - 1):
                positions[component4] = positions[component4] + value
            elif (positions[component4] + value) > (homepos - 1):
                if component4 == 0:
                    positions[component4] = (homepos)
                elif component4 == 1:
                    positions[component4] = (homepos + 1)
                elif component4 == 2:
                    positions[component4] = (homepos + 2)
                elif component4 == 3:
                    positions[component4] = (homepos + 3)
            positions1, positions2, positions3 = clipped(win, positions[component4], player, positions1, positions2, positions3)
            marker_move(win, positions[component4], mplay2)
    else:
        if mstart1.clicked(pt):
            positions[component1] = positions[component1] + startpos
            positions1, positions2, positions3 = clipped(win, positions[component1], player, positions1, positions2, positions3)
            marker_move(win, positions[component1], mstart1)
        elif mstart2.clicked(pt):
            positions[component2] = positions[component2] + startpos
            positions1, positions2, positions3 = clipped(win, positions[component2], player, positions1, positions2, positions3)
            marker_move(win, positions[component2], mstart2)
        elif mplay1.clicked(pt):
            if (positions[component3] + value) > 67 and positions[component3] < 68:
                dif = 67 - positions[component3]
                positions[component3] = 15 + (value-dif)
            elif positions[component3] < (startpos) and (positions[component3] + value) > (startpos - 1):
                dif = (startpos) - positions[component3]
                if value == 6:
                    if dif == 1:
                        if component3 == 0:
                            positions[component3] = (homepos)
                        elif component3 == 1:
                            positions[component3] = (homepos + 1)
                        elif component3 == 2:
                            positions[component3] = (homepos + 2)
                        elif component3 == 3:
                            positions[component3] = (homepos + 3)
                    else:
                        positions[component3] = arrowpos + (value-dif)
                else:
                    positions[component3] = arrowpos + (value-dif)
            elif (positions[component3] + value) > (homepos - 1):
                if component3 == 0:
                    positions[component3] = homepos
                elif component3 == 1:
                    positions[component3] = homepos + 1
                elif component3 == 2:
                    positions[component3] = homepos + 2
                elif component3 == 3:
                    positions[component3] = homepos + 3
            else:
                positions[component3] = positions[component3] + value
            positions1, positions2, positions3 = clipped(win, positions[component3], player, positions1, positions2, positions3)
            marker_move(win, positions[component3], mplay1)
        elif mplay2.clicked(pt):
            if (positions[component4] + value) > 67 and positions[component4] < 68:
                dif = 67 - positions[component4]
                positions[component4] = 15 + (value-dif)
            elif positions[component4] < (startpos) and (positions[component4] + value) > (startpos - 1):
                dif = (startpos) - positions[component4]
                if value == 6:
                    if dif == 1:
                        if component4 == 0:
                            positions[component4] = (homepos)
                        elif component4 == 1:
                            positions[component4] = (homepos + 1)
                        elif component4 == 2:
                            positions[component4] = (homepos + 2)
                        elif component4 == 3:
                            positions[component4] = (homepos + 3)
                    else:
                        positions[component4] = arrowpos + (value-dif)
                else:
                    positions[component4] = arrowpos + (value-dif)
            elif (positions[component4] + value) > (homepos - 1):
                if component4 == 0:
                    positions[component4] = homepos
                elif component4 == 1:
                    positions[component4] = homepos + 1
                elif component4 == 2:
                    positions[component4] = homepos + 2
                elif component4 == 3:
                    positions[component4] = homepos + 3
            else:
                positions[component4] = positions[component4] + value
            positions1, positions2, positions3 = clipped(win, positions[component4], player, positions1, positions2, positions3)
            marker_move(win, positions[component4], mplay2)
    
                
def psmoves3(win, player, positions, mstart1, mstart2, mstart3, component1, component2, component3, positions1, positions2, positions3):
    pt = win.getMouse()
    while not (mstart1.clicked(pt) or mstart2.clicked(pt) or mstart3.clicked(pt)):
        pt = win.getMouse()
    if player == "player1":
        if mstart1.clicked(pt):
            positions[component1] = positions[component1] + 16
            positions1, positions2, positions3 = clipped(win, positions[component1], player, positions1, positions2, positions3)
            marker_move(win, positions[component1], mstart1)
        if mstart2.clicked(pt):
            positions[component2] = positions[component2] + 16
            positions1, positions2, positions3 = clipped(win, positions[component2], player, positions1, positions2, positions3)
            marker_move(win, positions[component2], mstart2)
        if mstart3.clicked(pt):
            positions[component3] = positions[component3] + 16
            positions1, positions2, positions3 = clipped(win, positions[component3], player, positions1, positions2, positions3)
            marker_move(win, positions[component3], mstart3)
    elif player == "player2":
        if mstart1.clicked(pt):
            positions[component1] = positions[component1] + 29
            positions1, positions2, positions3 = clipped(win, positions[component1], player, positions1, positions2, positions3)
            marker_move(win, positions[component1], mstart1)
        if mstart2.clicked(pt):
            positions[component2] = positions[component2] + 29
            positions1, positions2, positions3 = clipped(win, positions[component2], player, positions1, positions2, positions3)
            marker_move(win, positions[component2], mstart2)
        if mstart3.clicked(pt):
            positions[component3] = positions[component3] + 29
            positions1, positions2, positions3 = clipped(win, positions[component3], player, positions1, positions2, positions3)
            marker_move(win, positions[component3], mstart3)
    elif player == "player3":
        if mstart1.clicked(pt):
            positions[component1] = positions[component1] + 42
            positions1, positions2, positions3 = clipped(win, positions[component1], player, positions1, positions2, positions3)
            marker_move(win, positions[component1], mstart1)
        if mstart2.clicked(pt):
            positions[component2] = positions[component2] + 42
            positions1, positions2, positions3 = clipped(win, positions[component2], player, positions1, positions2, positions3)
            marker_move(win, positions[component2], mstart2)
        if mstart3.clicked(pt):
            positions[component3] = positions[component3] + 42
            positions1, positions2, positions3 = clipped(win, positions[component3], player, positions1, positions2, positions3)
            marker_move(win, positions[component3], mstart3)
    elif player == "player4":
        if mstart1.clicked(pt):
            positions[component1] = positions[component1] + 55
            positions1, positions2, positions3 = clipped(win, positions[component1], player, positions1, positions2, positions3)
            marker_move(win, positions[component1], mstart1)
        if mstart2.clicked(pt):
            positions[component2] = positions[component2] + 55
            positions1, positions2, positions3 = clipped(win, positions[component2], player, positions1, positions2, positions3)
            marker_move(win, positions[component2], mstart2)
        if mstart3.clicked(pt):
            positions[component3] = positions[component3] + 55
            positions1, positions2, positions3 = clipped(win, positions[component3], player, positions1, positions2, positions3)
            marker_move(win, positions[component3], mstart3)

    return positions, positions1, positions2, positions3

def psmoves2(win, player, positions, mstart1, mstart2, component1, component2, positions1, positions2, positions3):
    pt = win.getMouse()
    while not (mstart1.clicked(pt) or mstart2.clicked(pt)):
        pt = win.getMouse()
    if player == "player1":
        if mstart1.clicked(pt):
            positions[component1] = positions[component1] + 16
            positions1, positions2, positions3 = clipped(win, positions[component1], player, positions1, positions2, positions3)
            marker_move(win, positions[component1], mstart1)
        if mstart2.clicked(pt):
            positions[component2] = positions[component2] + 16
            positions1, positions2, positions3 = clipped(win, positions[component2], player, positions1, positions2, positions3)
            marker_move(win, positions[component2], mstart2)
    elif player == "player2":
        if mstart1.clicked(pt):
            positions[component1] = positions[component1] + 29
            positions1, positions2, positions3 = clipped(win, positions[component1], player, positions1, positions2, positions3)
            marker_move(win, positions[component1], mstart1)
        if mstart2.clicked(pt):
            positions[component2] = positions[component2] + 29
            positions1, positions2, positions3 = clipped(win, positions[component2], player, positions1, positions2, positions3)
            marker_move(win, positions[component2], mstart2)
    elif player == "player3":
        if mstart1.clicked(pt):
            positions[component1] = positions[component1] + 42
            positions1, positions2, positions3 = clipped(win, positions[component1], player, positions1, positions2, positions3)
            marker_move(win, positions[component1], mstart1)
        if mstart2.clicked(pt):
            positions[component2] = positions[component2] + 42
            positions1, positions2, positions3 = clipped(win, positions[component2], player, positions1, positions2, positions3)
            marker_move(win, positions[component2], mstart2)
    elif player == "player4":
        if mstart1.clicked(pt):
            positions[component1] = positions[component1] + 55
            positions1, positions2, positions3 = clipped(win, positions[component1], player, positions1, positions2, positions3)
            marker_move(win, positions[component1], mstart1)
        if mstart2.clicked(pt):
            positions[component2] = positions[component2] + 55
            positions1, positions2, positions3 = clipped(win, positions[component2], player, positions1, positions2, positions3)
            marker_move(win, positions[component2], mstart2)

    return positions, positions1, positions2, positions3

def psmoves1(win, player, positions, mstart1, component1, positions1, positions2, positions3):
    pt = win.getMouse()
    while not mstart1.clicked(pt):
        pt = win.getMouse()
    if player == "player1":
        if mstart1.clicked(pt):
            positions[component1] = positions[component1] + 16
            positions1, positions2, positions3 = clipped(win, positions[component1], player, positions1, positions2, positions3)
            marker_move(win, positions[component1], mstart1)
    elif player == "player2":
        if mstart1.clicked(pt):
            positions[component1] = positions[component1] + 29
            positions1, positions2, positions3 = clipped(win, positions[component1], player, positions1, positions2, positions3)
            marker_move(win, positions[component1], mstart1)
    elif player == "player3":
        if mstart1.clicked(pt):
            positions[component1] = positions[component1] + 42
            positions1, positions2, positions3 = clipped(win, positions[component1], player, positions1, positions2, positions3)
            marker_move(win, positions[component1], mstart1)
    elif player == "player4":
        if mstart1.clicked(pt):
            positions[component1] = positions[component1] + 55
            positions1, positions2, positions3 = clipped(win, positions[component1], player, positions1, positions2, positions3)
            marker_move(win, positions[component1], mstart1)

    return positions, positions1, positions2, positions3

def pmoves6_0(win, player, positions, m1, m2, m3, m4, positions1, positions2, positions3):
    pt = win.getMouse()
    while not (m1.clicked(pt) or m2.clicked(pt) or m3.clicked(pt) or m4.clicked(pt)):
        pt = win.getMouse()
    if player == "player1":
        pmoves6_0helper(win, pt, player, positions, m1, m2, m3, m4, 16, positions1, positions2, positions3)
    elif player == "player2":
        pmoves6_0helper(win, pt, player, positions, m1, m2, m3, m4, 29, positions1, positions2, positions3)
    elif player == "player3":
        pmoves6_0helper(win, pt, player, positions, m1, m2, m3, m4, 42, positions1, positions2, positions3)
    elif player == "player4":
        pmoves6_0helper(win, pt, player, positions, m1, m2, m3, m4, 55, positions1, positions2, positions3)

    return positions, positions1, positions2, positions3

def pmoves6_0helper(win, pt, player, positions, m1, m2, m3, m4, n, positions1, positions2, positions3):
    if m1.clicked(pt):
        positions[0] = positions[0] + n
        positions1, positions2, positions3 = clipped(win, positions[0], player, positions1, positions2, positions3)
        marker_move(win, positions[0], m1)
    if m2.clicked(pt):
        positions[1] = positions[1] + n
        positions1, positions2, positions3 = clipped(win, positions[1], player, positions1, positions2, positions3)
        marker_move(win, positions[1], m2)
    if m3.clicked(pt):
        positions[2] = positions[2] + n
        positions1, positions2, positions3 = clipped(win, positions[2], player, positions1, positions2, positions3)
        marker_move(win, positions[2], m3)
    if m4.clicked(pt):
        positions[3] = positions[3] + n
        positions1, positions2, positions3 = clipped(win, positions[3], player, positions1, positions2, positions3)
        marker_move(win, positions[3], m4)

def pmoves6_1(win, player, positions, mstart1, mstart2, mstart3,
              mplay1, component1, component2, component3, component4, positions1, positions2, positions3):
    pt = win.getMouse()
    while not (mstart1.clicked(pt) or mstart2.clicked(pt) or mstart3.clicked(pt) or mplay1.clicked(pt)):
        pt = win.getMouse()
    if player == "player1":
        pmoves6_1helper(win, pt, player, positions, mstart1, mstart2, mstart3,
                        mplay1, component1, component2, component3, component4,
                        16, 68, 73, positions1, positions2, positions3)
    elif player == "player2":
        pmoves6_1helper(win, pt, player, positions, mstart1, mstart2, mstart3,
                        mplay1, component1, component2, component3, component4,
                        29, 77, 82, positions1, positions2, positions3)
    elif player == "player3":
        pmoves6_1helper(win, pt, player, positions, mstart1, mstart2, mstart3,
                        mplay1, component1, component2, component3, component4,
                        42, 86, 91, positions1, positions2, positions3)
    elif player == "player4":
        pmoves6_1helper(win, pt, player, positions, mstart1, mstart2, mstart3,
                        mplay1, component1, component2, component3, component4,
                        55, 95, 100, positions1, positions2, positions3)

    return positions, positions1, positions2, positions3

def pmoves6_1helper(win, pt, player, positions, mstart1, mstart2, mstart3,
                    mplay1, component1, component2, component3, component4,
                    startpos, arrowpos, homepos, positions1, positions2, positions3):
    if player == "player1":
        if mstart1.clicked(pt):
            positions[component1] = positions[component1] + 16
            positions1, positions2, positions3 = clipped(win, positions[component1], player, positions1, positions2, positions3)
            marker_move(win, positions[component1], mstart1)
        elif mstart2.clicked(pt):
            positions[component2] = positions[component2] + 16
            positions1, positions2, positions3 = clipped(win, positions[component2], player, positions1, positions2, positions3)
            marker_move(win, positions[component2], mstart2)
        elif mstart3.clicked(pt):
            positions[component3] = positions[component3] + 16
            positions1, positions2, positions3 = clipped(win, positions[component3], player, positions1, positions2, positions3)
            marker_move(win, positions[component3], mstart3)
        else:
            if (positions[component4] + 6) <= 72:
                positions[component4] = positions[component4] + 6
            elif (positions[component4] + 6) > 72:
                if component4 == 0:
                    positions[component4] = 73
                elif component4 == 1:
                    positions[component4] = 74
                elif component4 == 2:
                    positions[component4] = 75
                elif component4 == 3:
                    positions[component4] = 76
            positions1, positions2, positions3 = clipped(win, positions[component4], player, positions1, positions2, positions3)
            marker_move(win, positions[component4], mplay1)
    else:
        if mstart1.clicked(pt):
            positions[component1] = positions[component1] + startpos
            positions1, positions2, positions3 = clipped(win, positions[component1], player, positions1, positions2, positions3)
            marker_move(win, positions[component1], mstart1)
        elif mstart2.clicked(pt):
            positions[component2] = positions[component2] + startpos
            positions1, positions2, positions3 = clipped(win, positions[component2], player, positions1, positions2, positions3)
            marker_move(win, positions[component2], mstart2)
        elif mstart3.clicked(pt):
            positions[component3] = positions[component3] + startpos
            positions1, positions2, positions3 = clipped(win, positions[component3], player, positions1, positions2, positions3)
            marker_move(win, positions[component3], mstart3)
        else:
            if (positions[component4] + 6) > 67 and positions[component4] < 68:
                dif = 67 - positions[component4]
                positions[component4] = 15 + (6-dif)
            elif positions[component4] < startpos and (positions[component4] + 6) > (startpos - 1):
                dif = startpos - positions[component4]
                if dif == 1:
                    if component4 == 0:
                        positions[component4] = homepos
                    elif component4 == 1:
                        positions[component4] = homepos + 1
                    elif component4 == 2:
                        positions[component4] = homepos + 2
                    elif component4 == 3:
                        positions[component4] = homepos + 3
                else:
                    positions[component4] = arrowpos + (6-dif)
            elif (positions[component4] + 6) > (homepos - 1):
                if component4 == 0:
                    positions[component4] = homepos
                elif component4 == 1:
                    positions[component4] = homepos + 1
                elif component4 == 2:
                    positions[component4] = homepos + 2
                elif component4 == 3:
                    positions[component4] = homepos + 3
            else:
                positions[component4] = positions[component4] + 6
            positions1, positions2, positions3 = clipped(win, positions[component4], player, positions1, positions2, positions3)
            marker_move(win, positions[component4], mplay1)

def pmoves6_2(win, player, positions, mstart1, mstart2, mplay1, mplay2, component1, component2, component3, component4, positions1, positions2, positions3):
    pt = win.getMouse()
    while not (mstart1.clicked(pt) or mstart2.clicked(pt) or mplay1.clicked(pt) or mplay2.clicked(pt)):
        pt = win.getMouse()
    if player == "player1":
        pmoves6_2helper(win, pt, player, positions, mstart1, mstart2, mplay1,
                        mplay2, component1, component2, component3, component4,
                        16, 68, 73, positions1, positions2, positions3)
    elif player == "player2":
        pmoves6_2helper(win, pt, player, positions, mstart1, mstart2, mplay1,
                        mplay2, component1, component2, component3, component4,
                        29, 77, 82, positions1, positions2, positions3)
    elif player == "player3":
        pmoves6_2helper(win, pt, player, positions, mstart1, mstart2, mplay1,
                        mplay2, component1, component2, component3, component4,
                        42, 86, 91, positions1, positions2, positions3)
    elif player == "player4":
        pmoves6_2helper(win, pt, player, positions, mstart1, mstart2, mplay1,
                        mplay2, component1, component2, component3, component4,
                        55, 95, 100, positions1, positions2, positions3)

    return positions, positions1, positions2, positions3

def pmoves6_2helper(win, pt, player, positions, mstart1, mstart2, mplay1,
                    mplay2, component1, component2, component3, component4,
                    startpos, arrowpos, homepos, positions1, positions2, positions3):
    if player == "player1":
        if mstart1.clicked(pt):
            positions[component1] = positions[component1] + 16
            positions1, positions2, positions3 = clipped(win, positions[component1], player, positions1, positions2, positions3)
            marker_move(win, positions[component1], mstart1)
        elif mstart2.clicked(pt):
            positions[component2] = positions[component2] + 16
            positions1, positions2, positions3 = clipped(win, positions[component2], player, positions1, positions2, positions3)
            marker_move(win, positions[component2], mstart2)
        elif mplay1.clicked(pt):
            if (positions[component3] + 6) <= 72:
                positions[component3] = positions[component3] + 6
            elif (positions[component3] + 6) > 72:
                if component3 == 0:
                    positions[component3] = 73
                elif component3 == 1:
                    positions[component3] = 74
                elif component3 == 2:
                    positions[component3] = 75
                elif component3 == 3:
                    positions[component3] = 76
            positions1, positions2, positions3 = clipped(win, positions[component3], player, positions1, positions2, positions3)
            marker_move(win, positions[component3], mplay1)
        else:
            if (positions[component4] + 6) <= 72:
                positions[component4] = positions[component4] + 6
            elif (positions[component4] + 6) > 72:
                if component4 == 0:
                    positions[component4] = 73
                elif component4 == 1:
                    positions[component4] = 74
                elif component4 == 2:
                    positions[component4] = 75
                elif component4 == 3:
                    positions[component4] = 76
            positions1, positions2, positions3 = clipped(win, positions[component4], player, positions1, positions2, positions3)
            marker_move(win, positions[component4], mplay2)
    else:
        if mstart1.clicked(pt):
            positions[component1] = positions[component1] + startpos
            positions1, positions2, positions3 = clipped(win, positions[component1], player, positions1, positions2, positions3)
            marker_move(win, positions[component1], mstart1)
        elif mstart2.clicked(pt):
            positions[component2] = positions[component2] + startpos
            positions1, positions2, positions3 = clipped(win, positions[component2], player, positions1, positions2, positions3)
            marker_move(win, positions[component2], mstart2)
        elif mplay1.clicked(pt):
            if (positions[component3] + 6) > 67 and positions[component3] < 68:
                dif = 67 - positions[component3]
                positions[component3] = 15 + (6-dif)
            elif positions[component3] < startpos and (positions[component3] + 6) > (startpos - 1):
                dif = startpos - positions[component3]
                if dif == 1:
                    if component3 == 0:
                        positions[component3] = homepos
                    elif component3 == 1:
                        positions[component3] = homepos + 1
                    elif component3 == 2:
                        positions[component3] = homepos + 2
                    elif component3 == 3:
                        positions[component3] = homepos + 3
                else:
                    positions[component3] = arrowpos + (6-dif)
            elif (positions[component3] + 6) > (homepos - 1):
                if component3 == 0:
                    positions[component3] = homepos
                elif component3 == 1:
                    positions[component3] = homepos + 1
                elif component3 == 2:
                    positions[component3] = homepos + 2
                elif component3 == 3:
                    positions[component3] = homepos + 3
            else:
                positions[component3] = positions[component3] + 6
            positions1, positions2, positions3 = clipped(win, positions[component3], player, positions1, positions2, positions3)
            marker_move(win, positions[component3], mplay1)
        else:
            if (positions[component4] + 6) > 67 and positions[component4] < 68:
                dif = 67 - positions[component4]
                positions[component4] = 15 + (6-dif)
            elif positions[component4] < startpos and (positions[component4] + 6) > (startpos - 1):
                dif = startpos - positions[component4]
                if dif == 1:
                    if component4 == 0:
                        positions[component4] = homepos
                    elif component4 == 1:
                        positions[component4] = homepos + 1
                    elif component4 == 2:
                        positions[component4] = homepos + 2
                    elif component4 == 3:
                        positions[component4] = homepos + 3
                else:
                    positions[component4] = arrowpos + (6-dif)
            elif (positions[component4] + 6) > (homepos - 1):
                if component4 == 0:
                    positions[component4] = homepos
                elif component4 == 1:
                    positions[component4] = homepos + 1
                elif component4 == 2:
                    positions[component4] = homepos + 2
                elif component4 == 3:
                    positions[component4] = homepos + 3
            else:
                positions[component4] = positions[component4] + 6
            positions1, positions2, positions3 = clipped(win, positions[component4], player, positions1, positions2, positions3)
            marker_move(win, positions[component4], mplay2)

def pmoves6_3(win, player, positions, mstart1, mplay1, mplay2, mplay3, component1, component2, component3, component4, positions1, positions2, positions3):
    pt = win.getMouse()
    while not (mstart1.clicked(pt) or mplay1.clicked(pt) or mplay2.clicked(pt) or mplay3.clicked(pt)):
        pt = win.getMouse()
    if player == "player1":
        pmoves6_3helper(win, pt, player, positions, mstart1, mplay1, mplay2,
                        mplay3, component1, component2, component3, component4,
                        16, 68, 73, positions1, positions2, positions3)
    elif player == "player2":
        pmoves6_3helper(win, pt, player, positions, mstart1, mplay1, mplay2,
                        mplay3, component1, component2, component3, component4,
                        29, 77, 82, positions1, positions2, positions3)
    elif player == "player3":
        pmoves6_3helper(win, pt, player, positions, mstart1, mplay1, mplay2,
                        mplay3, component1, component2, component3, component4,
                        42, 86, 91, positions1, positions2, positions3)
    elif player == "player4":
        pmoves6_3helper(win, pt, player, positions, mstart1, mplay1, mplay2,
                        mplay3, component1, component2, component3, component4,
                        55, 95, 100, positions1, positions2, positions3)

    return positions, positions1, positions2, positions3

def pmoves6_3helper(win, pt, player, positions, mstart1, mplay1, mplay2,
                    mplay3, component1, component2, component3, component4,
                    startpos, arrowpos, homepos, positions1, positions2, positions3):
    if player == "player1":
        if mstart1.clicked(pt):
            positions[component1] = positions[component1] + 16
            positions1, positions2, positions3 = clipped(win, positions[component1], player, positions1, positions2, positions3)
            marker_move(win, positions[component1], mstart1)
        elif mplay1.clicked(pt):
            if (positions[component2] + 6) <= 72:
                positions[component2] = positions[component2] + 6
            elif (positions[component2] + 6) > 72:
                if component2 == 0:
                    positions[component2] = 73
                elif component2 == 1:
                    positions[component2] = 74
                elif component2 == 2:
                    positions[component2] = 75
                elif component2 == 3:
                    positions[component2] = 76
            positions1, positions2, positions3 = clipped(win, positions[component2], player, positions1, positions2, positions3)
            marker_move(win, positions[component2], mplay1)
        elif mplay2.clicked(pt):
            if (positions[component3] + 6) <= 72:
                positions[component3] = positions[component3] + 6
            elif (positions[component3] + 6) > 72:
                if component3 == 0:
                    positions[component3] = 73
                elif component3 == 1:
                    positions[component3] = 74
                elif component3 == 2:
                    positions[component3] = 75
                elif component3 == 3:
                    positions[component3] = 76
            positions1, positions2, positions3 = clipped(win, positions[component3], player, positions1, positions2, positions3)
            marker_move(win, positions[component3], mplay2)
        else:
            if (positions[component4] + 6) <= 72:
                positions[component4] = positions[component4] + 6
            elif (positions[component4] + 6) > 72:
                if component4 == 0:
                    positions[component4] = 73
                elif component4 == 1:
                    positions[component4] = 74
                elif component4 == 2:
                    positions[component4] = 75
                elif component4 == 3:
                    positions[component4] = 76
            positions1, positions2, positions3 = clipped(win, positions[component4], player, positions1, positions2, positions3)
            marker_move(win, positions[component4], mplay3)
    else:
        if mstart1.clicked(pt):
            positions[component1] = positions[component1] + startpos
            positions1, positions2, positions3 = clipped(win, positions[component1], player, positions1, positions2, positions3)
            marker_move(win, positions[component1], mstart1)
        elif mplay1.clicked(pt):
            if (positions[component2] + 6) > 67 and positions[component2] < 68:
                dif = 67 - positions[component2]
                positions[component2] = 15 + (6-dif)
            elif positions[component2] < startpos and (positions[component2] + 6) > (startpos - 1):
                dif = startpos - positions[component2]
                if dif == 1:
                    if component2 == 0:
                        positions[component2] = homepos
                    elif component2 == 1:
                        positions[component2] = homepos + 1
                    elif component2 == 2:
                        positions[component2] = homepos + 2
                    elif component2 == 3:
                        positions[component2] = homepos + 3
                else:
                    positions[component2] = arrowpos + (6-dif)
            elif (positions[component2] + 6) > (homepos - 1):
                if component2 == 0:
                    positions[component2] = homepos
                elif component2 == 1:
                    positions[component2] = homepos + 1
                elif component2 == 2:
                    positions[component2] = homepos + 2
                elif component2 == 3:
                    positions[component2] = homepos + 3
            else:
                positions[component2] = positions[component2] + 6
            positions1, positions2, positions3 = clipped(win, positions[component2], player, positions1, positions2, positions3)
            marker_move(win, positions[component2], mplay1)
        elif mplay2.clicked(pt):
            if (positions[component3] + 6) > 67 and positions[component3] < 68:
                dif = 67 - positions[component3]
                positions[component3] = 15 + (6-dif)
            elif positions[component3] < startpos and (positions[component3] + 6) > (startpos - 1):
                dif = startpos - positions[component3]
                if dif == 1:
                    if component3 == 0:
                        positions[component3] = homepos
                    elif component3 == 1:
                        positions[component3] = homepos + 1
                    elif component3 == 2:
                        positions[component3] = homepos + 2
                    elif component3 == 3:
                        positions[component3] = homepos + 3
                else:
                    positions[component3] = arrowpos + (6-dif)
            elif (positions[component3] + 6) > (homepos - 1):
                if component3 == 0:
                    positions[component3] = homepos
                elif component3 == 1:
                    positions[component3] = homepos + 1
                elif component3 == 2:
                    positions[component3] = homepos + 2
                elif component3 == 3:
                    positions[component3] = homepos + 3
            else:
                positions[component3] = positions[component3] + 6
            positions1, positions2, positions3 = clipped(win, positions[component3], player, positions1, positions2, positions3)
            marker_move(win, positions[component3], mplay2)
        else:
            if (positions[component4] + 6) > 67 and positions[component4] < 68:
                dif = 67 - positions[component4]
                positions[component4] = 15 + (6-dif)
            elif positions[component4] < startpos and (positions[component4] + 6) > (startpos - 1):
                dif = startpos - positions[component4]
                if dif == 1:
                    if component4 == 0:
                        positions[component4] = homepos
                    elif component4 == 1:
                        positions[component4] = homepos + 1
                    elif component4 == 2:
                        positions[component4] = homepos + 2
                    elif component4 == 3:
                        positions[component4] = homepos + 3
                else:
                    positions[component4] = arrowpos + (6-dif)
            elif (positions[component4] + 6) > (homepos - 1):
                if component4 == 0:
                    positions[component4] = homepos
                elif component4 == 1:
                    positions[component4] = homepos + 1
                elif component4 == 2:
                    positions[component4] = homepos + 2
                elif component4 == 3:
                    positions[component4] = homepos + 3
            else:
                positions[component4] = positions[component4] + 6
            positions1, positions2, positions3 = clipped(win, positions[component4], player, positions1, positions2, positions3)
            marker_move(win, positions[component4], mplay3)


def pmoves1(win, player, positions, value, m1, component1, positions1, positions2, positions3):
    pt = win.getMouse()
    while not m1.clicked(pt):
        pt = win.getMouse()
    if player == "player1":
        pmoves1helper(win, pt, player, positions, value, m1, component1, 16, 68, 73, positions1, positions2, positions3)
    elif player == "player2":
        pmoves1helper(win, pt, player, positions, value, m1, component1, 29, 77, 82, positions1, positions2, positions3)
    elif player == "player3":
        pmoves1helper(win, pt, player, positions, value, m1, component1, 42, 86, 91, positions1, positions2, positions3)
    elif player == "player4":
        pmoves1helper(win, pt, player, positions, value, m1, component1, 55, 95, 100, positions1, positions2, positions3)

    return positions, positions1, positions2, positions3

def pmoves1helper(win, pt, player, positions, value, m1, component1, startpos, arrowpos,
                  homepos, positions1, positions2, positions3):
    if player == "player1":
        if m1.clicked(pt):
            if (positions[component1] + value) <= (homepos - 1):
                positions[component1] = positions[component1] + value
            elif (positions[component1] + value) > (homepos - 1):
                if component1 == 0:
                    positions[component1] = homepos
                elif component1 == 1:
                    positions[component1] = homepos + 1
                elif component1 == 2:
                    positions[component1] = homepos + 2
                elif component1 == 3:
                    positions[component1] = homepos + 3
            positions1, positions2, positions3 = clipped(win, positions[component1], player, positions1, positions2, positions3)
            marker_move(win, positions[component1], m1)
    else:
        if m1.clicked(pt):
            if (positions[component1] + value) > 67 and positions[component1] < 68:
                dif = 67 - positions[component1]
                positions[component1] = 15 + (value-dif)
            elif positions[component1] < startpos and (positions[component1] + value) > (startpos - 1):
                dif = startpos - positions[component1]
                positions[component1] = arrowpos + (value-dif)
            elif (positions[component1] + value) > (homepos - 1):
                if component1 == 0:
                    positions[component1] = homepos
                elif component1 == 1:
                    positions[component1] = homepos + 1
                elif component1 == 2:
                    positions[component1] = homepos + 2
                elif component1 == 3:
                    positions[component1] = homepos + 3
            else:
                positions[component1] = positions[component1] + value
            positions1, positions2, positions3 = clipped(win, positions[component1], player, positions1, positions2, positions3)
            marker_move(win, positions[component1], m1)
    

def pmoves2(win, player, positions, value, m1, m2, component1, component2, positions1, positions2, positions3):
    pt = win.getMouse()
    while not (m1.clicked(pt) or m2.clicked(pt)):
        pt = win.getMouse()
    if player == "player1":
        pmoves2helper(win, pt, player, positions, value, m1, m2, component1, component2, 16, 68, 73, positions1, positions2, positions3)
    elif player == "player2":
        pmoves2helper(win, pt, player, positions, value, m1, m2, component1, component2, 29, 77, 82, positions1, positions2, positions3)
    elif player == "player3":
        pmoves2helper(win, pt, player, positions, value, m1, m2, component1, component2, 42, 86, 91, positions1, positions2, positions3)
    elif player == "player4":
        pmoves2helper(win, pt, player, positions, value, m1, m2, component1, component2, 55, 95, 100, positions1, positions2, positions3)

    return positions, positions1, positions2, positions3

def pmoves2helper(win, pt, player, positions, value, m1, m2, component1,
                  component2, startpos, arrowpos, homepos, positions1, positions2, positions3):
    if player == "player1":
        if m1.clicked(pt):
            if (positions[component1] + value) <= (homepos - 1):
                positions[component1] = positions[component1] + value
            elif (positions[component1] + value) > (homepos - 1):
                if component1 == 0:
                    positions[component1] = homepos
                elif component1 == 1:
                    positions[component1] = homepos + 1
                elif component1 == 2:
                    positions[component1] = homepos + 2
                elif component1 == 3:
                    positions[component1] = homepos + 3
            positions1, positions2, positions3 = clipped(win, positions[component1], player, positions1, positions2, positions3)
            marker_move(win, positions[component1], m1)
        elif m2.clicked(pt):
            if (positions[component2] + value) <= (homepos - 1):
                positions[component2] = positions[component2] + value
            elif (positions[component2] + value) > (homepos - 1):
                if component2 == 0:
                    positions[component2] = homepos
                elif component2 == 1:
                    positions[component2] = homepos + 1
                elif component2 == 2:
                    positions[component2] = homepos + 2
                elif component2 == 3:
                    positions[component2] = homepos + 3
            positions1, positions2, positions3 = clipped(win, positions[component2], player, positions1, positions2, positions3)
            marker_move(win, positions[component2], m2)
    else:
        if m1.clicked(pt):
            if (positions[component1] + value) > 67 and positions[component1] < 68:
                dif = 67 - positions[component1]
                positions[component1] = 15 + (value-dif)
            elif positions[component1] < startpos and (positions[component1] + value) > (startpos - 1):
                dif = startpos - positions[component1]
                positions[component1] = arrowpos + (value-dif)
            elif (positions[component1] + value) > (homepos - 1):
                if component1 == 0:
                    positions[component1] = homepos
                elif component1 == 1:
                    positions[component1] = homepos + 1
                elif component1 == 2:
                    positions[component1] = homepos + 2
                elif component1 == 3:
                    positions[component1] = homepos + 3
            else:
                positions[component1] = positions[component1] + value
            positions1, positions2, positions3 = clipped(win, positions[component1], player, positions1, positions2, positions3)
            marker_move(win, positions[component1], m1)
        elif m2.clicked(pt):
            if (positions[component2] + value) > 67 and positions[component2] < 68:
                dif = 67 - positions[component2]
                positions[component2] = 15 + (value-dif)
            elif positions[component2] < startpos and (positions[component2] + value) > (startpos - 1):
                dif = startpos - positions[component2]
                positions[component2] = arrowpos + (value-dif)
            elif (positions[component2] + value) > (homepos - 1):
                if component2 == 0:
                    positions[component2] = homepos
                elif component2 == 1:
                    positions[component2] = homepos + 1
                elif component2 == 2:
                    positions[component2] = homepos + 2
                elif component2 == 3:
                    positions[component2] = homepos + 3
            else:
                positions[component2] = positions[component2] + value
            positions1, positions2, positions3 = clipped(win, positions[component2], player, positions1, positions2, positions3)
            marker_move(win, positions[component2], m2)

def pmoves3(win, player, positions, value, m1, m2, m3, component1, component2, component3, positions1, positions2, positions3):
    pt = win.getMouse()
    while not (m1.clicked(pt) or m2.clicked(pt) or m3.clicked(pt)):
        pt = win.getMouse()
    if player == "player1":
        pmoves3helper(win, pt, player, positions, value, m1, m2, m3, component1, component2, component3, 16, 68, 73, positions1, positions2, positions3)
    elif player == "player2":
        pmoves3helper(win, pt, player, positions, value, m1, m2, m3, component1, component2, component3, 29, 77, 82, positions1, positions2, positions3)
    elif player == "player3":
        pmoves3helper(win, pt, player, positions, value, m1, m2, m3, component1, component2, component3, 42, 86, 91, positions1, positions2, positions3)
    elif player == "player4":
        pmoves3helper(win, pt, player, positions, value, m1, m2, m3, component1, component2, component3, 55, 95, 100, positions1, positions2, positions3)

    return positions, positions1, positions2, positions3

def pmoves3helper(win, pt, player, positions, value, m1, m2, m3, component1,
                  component2, component3, startpos, arrowpos, homepos, positions1, positions2, positions3):
    if player == "player1":
        if m1.clicked(pt):
            if (positions[component1] + value) <= (homepos - 1):
                positions[component1] = positions[component1] + value
            elif (positions[component1] + value) > (homepos - 1):
                if component1 == 0:
                    positions[component1] = homepos
                elif component1 == 1:
                    positions[component1] = homepos + 1
                elif component1 == 2:
                    positions[component1] = homepos + 2
                elif component1 == 3:
                    positions[component1] = homepos + 3
            positions1, positions2, positions3 = clipped(win, positions[component1], player, positions1, positions2, positions3)
            marker_move(win, positions[component1], m1)
        elif m2.clicked(pt):
            if (positions[component2] + value) <= (homepos - 1):
                positions[component2] = positions[component2] + value
            elif (positions[component2] + value) > (homepos - 1):
                if component2 == 0:
                    positions[component2] = homepos
                elif component2 == 1:
                    positions[component2] = homepos + 1
                elif component2 == 2:
                    positions[component2] = homepos + 2
                elif component2 == 3:
                    positions[component2] = homepos + 3
            positions1, positions2, positions3 = clipped(win, positions[component2], player, positions1, positions2, positions3)
            marker_move(win, positions[component2], m2)
        elif m3.clicked(pt):
            if (positions[component3] + value) <= (homepos - 1):
                positions[component3] = positions[component3] + value
            elif (positions[component3] + value) > (homepos - 1):
                if component3 == 0:
                    positions[component3] = homepos
                elif component3 == 1:
                    positions[component3] = homepos + 1
                elif component3 == 2:
                    positions[component3] = homepos + 2
                elif component3 == 3:
                    positions[component3] = homepos + 3
            positions1, positions2, positions3 = clipped(win, positions[component3], player, positions1, positions2, positions3)
            marker_move(win, positions[component3], m3)
    else:
        if m1.clicked(pt):
            if (positions[component1] + value) > 67 and positions[component1] < 68:
                dif = 67 - positions[component1]
                positions[component1] = 15 + (value-dif)
            elif positions[component1] < startpos and (positions[component1] + value) > (startpos - 1):
                dif = startpos - positions[component1]
                positions[component1] = arrowpos + (value-dif)
            elif (positions[component1] + value) > (homepos - 1):
                if component1 == 0:
                    positions[component1] = homepos
                elif component1 == 1:
                    positions[component1] = homepos + 1
                elif component1 == 2:
                    positions[component1] = homepos + 2
                elif component1 == 3:
                    positions[component1] = homepos + 3
            else:
                positions[component1] = positions[component1] + value
            positions1, positions2, positions3 = clipped(win, positions[component1], player, positions1, positions2, positions3)
            marker_move(win, positions[component1], m1)
        elif m2.clicked(pt):
            if (positions[component2] + value) > 67 and positions[component2] < 68:
                dif = 67 - positions[component2]
                positions[component2] = 15 + (value-dif)
            elif positions[component2] < startpos and (positions[component2] + value) > (startpos - 1):
                dif = startpos - positions[component2]
                positions[component2] = arrowpos + (value-dif)
            elif (positions[component2] + value) > (homepos - 1):
                if component2 == 0:
                    positions[component2] = homepos
                elif component2 == 1:
                    positions[component2] = homepos + 1
                elif component2 == 2:
                    positions[component2] = homepos + 2
                elif component2 == 3:
                    positions[component2] = homepos + 3
            else:
                positions[component2] = positions[component2] + value
            positions1, positions2, positions3 = clipped(win, positions[component2], player, positions1, positions2, positions3)
            marker_move(win, positions[component2], m2)
        elif m3.clicked(pt):
            if (positions[component3] + value) > 67 and positions[component3] < 68:
                dif = 67 - positions[component3]
                positions[component3] = 15 + (value-dif)
            elif positions[component3] < startpos and (positions[component3] + value) > (startpos - 1):
                dif = startpos - positions[component3]
                positions[component3] = arrowpos + (value-dif)
            elif (positions[component3] + value) > (homepos - 1):
                if component3 == 0:
                    positions[component3] = homepos
                elif component3 == 1:
                    positions[component3] = homepos + 1
                elif component3 == 2:
                    positions[component3] = homepos + 2
                elif component3 == 3:
                    positions[component3] = homepos + 3
            else:
                positions[component3] = positions[component3] + value
            positions1, positions2, positions3 = clipped(win, positions[component3], player, positions1, positions2, positions3)
            marker_move(win, positions[component3], m3)

def pmoves4(win, player, positions, value, m1, m2, m3, m4, positions1, positions2, positions3):
    pt = win.getMouse()
    while not (m1.clicked(pt) or m2.clicked(pt) or m3.clicked(pt) or m4.clicked(pt)):
        pt = win.getMouse()
    if player == "player1":
        pmoves4helper(win, pt, player, positions, value, m1, m2, m3, m4, 16, 68, 73, positions1, positions2, positions3)
    elif player == "player2":
        pmoves4helper(win, pt, player, positions, value, m1, m2, m3, m4, 29, 77, 82, positions1, positions2, positions3)
    elif player == "player3":
        pmoves4helper(win, pt, player, positions, value, m1, m2, m3, m4, 42, 86, 91, positions1, positions2, positions3)
    elif player == "player4":
        pmoves4helper(win, pt, player, positions, value, m1, m2, m3, m4, 55, 95, 100, positions1, positions2, positions3)

    return positions, positions1, positions2, positions3

def pmoves4helper(win, pt, player, positions, value, m1, m2, m3, m4, startpos, arrowpos, homepos, positions1, positions2, positions3):
    if player == "player1":
        if m1.clicked(pt):
            if (positions[0] + value) <= (homepos - 1):
                positions[0] = positions[0] + value
            elif (positions[0] + value) > (homepos - 1):
                positions[0] = homepos
            positions1, positions2, positions3 = clipped(win, positions[0], player, positions1, positions2, positions3)
            marker_move(win, positions[0], m1)
        if m2.clicked(pt):
            if (positions[1] + value) <= (homepos - 1):
                positions[1] = positions[1] + value
            elif (positions[1] + value) > (homepos - 1):
                positions[1] = (homepos + 1)
            positions1, positions2, positions3 = clipped(win, positions[1], player, positions1, positions2, positions3)
            marker_move(win, positions[1], m2)
        if m3.clicked(pt):
            if (positions[2] + value) <= (homepos - 1):
                positions[2] = positions[2] + value
            elif (positions[2] + value) > (homepos - 1):
                positions[2] = (homepos + 2)
            positions1, positions2, positions3 = clipped(win, positions[2], player, positions1, positions2, positions3)
            marker_move(win, positions[2], m3)
        if m4.clicked(pt):
            if (positions[3] + value) <= (homepos - 1):
                positions[3] = positions[3] + value
            elif (positions[3] + value) > (homepos - 1):
                positions[3] = (homepos + 3)
            positions1, positions2, positions3 = clipped(win, positions[3], player, positions1, positions2, positions3)
            marker_move(win, positions[3], m4)
    else:
        if m1.clicked(pt):
            if (positions[0] + value) > 67 and positions[0] < 68:
                dif = 67 - positions[0]
                positions[0] = 15 + (value-dif)
            elif positions[0] < startpos and (positions[0] + value) > (startpos - 1):
                dif = startpos - positions[0]
                positions[0] = arrowpos + (value-dif)
            elif (positions[0] + value) > (homepos - 1):
                positions[0] = homepos
            else:
                positions[0] = positions[0] + value
            positions1, positions2, positions3 = clipped(win, positions[0], player, positions1, positions2, positions3)
            marker_move(win, positions[0], m1)
        if m2.clicked(pt):
            if (positions[1] + value) > 67 and positions[1] < 68:
                dif = 67 - positions[0]
                positions[1] = 15 + (value-dif)
            elif positions[1] < startpos and (positions[1] + value) > (startpos - 1):
                dif = startpos - positions[1]
                positions[1] = arrowpos + (value-dif)
            elif (positions[1] + value) > (homepos - 1):
                positions[1] = homepos + 1
            else:
                positions[1] = positions[1] + value
            positions1, positions2, positions3 = clipped(win, positions[1], player, positions1, positions2, positions3)
            marker_move(win, positions[1], m2)
        if m3.clicked(pt):
            if (positions[2] + value) > 67 and positions[2] < 68:
                dif = 67 - positions[2]
                positions[2] = 15 + (value-dif)
            elif positions[2] < startpos and (positions[2] + value) > (startpos - 1):
                dif = startpos - positions[2]
                positions[2] = arrowpos + (value-dif)
            elif (positions[2] + value) > (homepos - 1):
                positions[2] = homepos + 2
            else:
                positions[2] = positions[2] + value
            positions1, positions2, positions3 = clipped(win, positions[2], player, positions1, positions2, positions3)
            marker_move(win, positions[2], m3)
        if m4.clicked(pt):
            if (positions[3] + value) > 67 and positions[3] < 68:
                dif = 67 - positions[3]
                positions[3] = 15 + (value-dif)
            elif positions[3] < startpos and (positions[3] + value) > (startpos - 1):
                dif = startpos - positions[3]
                positions[3] = arrowpos + (value-dif)
            elif (positions[3] + value) > (homepos - 1):
                positions[3] = homepos + 3
            else:
                positions[3] = positions[3] + value
            positions1, positions2, positions3 = clipped(win, positions[3], player, positions1, positions2, positions3)
            marker_move(win, positions[3], m4)

def markers(win, c1, c2, c3, c4):
    m1 = CButton(win, Point(9.5,57.5), 1.2,"1")
    m1.activate()
    m1.buttonColor(c1)
    m2 = CButton(win, Point(9.5,52.5), 1.2,"2")
    m2.activate()
    m2.buttonColor(c1)
    m3 = CButton(win, Point(9.5,47.5), 1.2,"3")
    m3.activate()
    m3.buttonColor(c1)
    m4 = CButton(win, Point(9.5,42.5), 1.2,"4")
    m4.activate()
    m4.buttonColor(c1)
    m5 = CButton(win, Point(42.5,9.5), 1.2,"1")
    m5.activate()
    m5.buttonColor(c2)
    m6 = CButton(win, Point(47.5,9.5), 1.2,"2")
    m6.activate()
    m6.buttonColor(c2)
    m7 = CButton(win, Point(52.5,9.5), 1.2,"3")
    m7.activate()
    m7.buttonColor(c2)
    m8 = CButton(win, Point(57.5,9.5), 1.2,"4")
    m8.activate()
    m8.buttonColor(c2)
    m9 = CButton(win, Point(90.5,42.5), 1.2,"1")
    m9.activate()
    m9.buttonColor(c3)
    m10 = CButton(win, Point(90.5,47.5), 1.2,"2")
    m10.activate()
    m10.buttonColor(c3)
    m11 = CButton(win, Point(90.5,52.5), 1.2,"3")
    m11.activate()
    m11.buttonColor(c3)
    m12 = CButton(win, Point(90.5,57.5), 1.2,"4")
    m12.activate()
    m12.buttonColor(c3)
    m13 = CButton(win, Point(57.5,90.5), 1.2,"1")
    m13.activate()
    m13.buttonColor(c4)
    m14 = CButton(win, Point(52.5,90.5), 1.2,"2")
    m14.activate()
    m14.buttonColor(c4)
    m15 = CButton(win, Point(47.5,90.5), 1.2,"3")
    m15.activate()
    m15.buttonColor(c4)
    m16 = CButton(win, Point(42.5,90.5), 1.2,"4")
    m16.activate()
    m16.buttonColor(c4)
    return m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12, m13, m14, m15, m16
    
def positions():
    p1s1 = Point(9.5,57.5)
    p1s2 = Point(9.5,52.5)
    p1s3 = Point(9.5,47.5)
    p1s4 = Point(9.5,42.5)
    p2s1 = Point(42.5,9.5)
    p2s2 = Point(47.5,9.5)
    p2s3 = Point(52.5,9.5)
    p2s4 = Point(57.5,9.5)
    p3s1 = Point(90.5,42.5)
    p3s2 = Point(90.5,47.5)
    p3s3 = Point(90.5,52.5)
    p3s4 = Point(90.5,57.5)
    p4s1 = Point(42.5,90.5)
    p4s2 = Point(47.5,90.5)
    p4s3 = Point(52.5,90.5)
    p4s4 = Point(57.5,90.5)
    p1 = Point(16.5,45)
    p2 = Point(21.5,45)
    p3 = Point(26.5,45)
    p4 = Point(31.5,45)
    p5 = Point(36.5,45)
    p6 = Point(41.5,45)
    p7 = Point(45,41.5)
    p8 = Point(45,36.5)
    p9 = Point(45,31.5)
    p10 = Point(45,26.5)
    p11 = Point(45,21.5)
    p12 = Point(45,16.5)
    p13 = Point(50,16.5)
    p14 = Point(55,16.5)
    p15 = Point(55,21.5)
    p16 = Point(55,26.5)
    p17 = Point(55,31.5)
    p18 = Point(55,36.5)
    p19 = Point(55,41.5)
    p20 = Point(58.5,45)
    p21 = Point(63.5,45)
    p22 = Point(68.5,45)
    p23 = Point(73.5,45)
    p24 = Point(78.5,45)
    p25 = Point(83.5,45)
    p26 = Point(83.5,50)
    p27 = Point(83.5,55)
    p28 = Point(78.5,55)
    p29 = Point(73.5,55)
    p30 = Point(68.5,55)
    p31 = Point(63.5,55)
    p32 = Point(58.5,55)
    p33 = Point(55,58.5)
    p34 = Point(55,63.5)
    p35 = Point(55,68.5)
    p36 = Point(55,73.5)
    p37 = Point(55,78.5)
    p38 = Point(55,83.5)
    p39 = Point(50,83.5)
    p40 = Point(45,83.5)
    p41 = Point(45,78.5)
    p42 = Point(45,73.5)
    p43 = Point(45,68.5)
    p44 = Point(45,63.5)
    p45 = Point(45,58.5)
    p46 = Point(41.5,55)
    p47 = Point(36.5,55)
    p48 = Point(31.5,55)
    p49 = Point(26.5,55)
    p50 = Point(21.5,55)
    p51 = Point(16.5,55)
    p52 = Point(16.5,50)
    p53 = Point(21.5,50)
    p54 = Point(26.5,50)
    p55 = Point(31.5,50)
    p56 = Point(36.5,50)
    p57 = Point(41.5,50)
    p58 = Point(48,50)
    p59 = Point(45,53)
    p60 = Point(45,47)
    p61 = Point(45,50)
    p62 = Point(50,21.5)
    p63 = Point(50,26.5)
    p64 = Point(50,31.5)
    p65 = Point(50,36.5)
    p66 = Point(50,41.5)
    p67 = Point(50,48)
    p68 = Point(47,45)
    p69 = Point(53,45)
    p70 = Point(50,45)
    p71 = Point(78.5,50)
    p72 = Point(73.5,50)
    p73 = Point(68.5,50)
    p74 = Point(63.5,50)
    p75 = Point(58.5,50)
    p76 = Point(52,50)
    p77 = Point(55,47)
    p78 = Point(55,53)
    p79 = Point(55,50)
    p80 = Point(50,78.5)
    p81 = Point(50,73.5)
    p82 = Point(50,68.5)
    p83 = Point(50,63.5)
    p84 = Point(50,58.5)
    p85 = Point(50,52)
    p86 = Point(53,55)
    p87 = Point(47,55)
    p88 = Point(50,55)
    return [p1s1,p1s2,p1s3,p1s4,p2s1,p2s2,p2s3,p2s4,p3s1,p3s2,p3s3,p3s4,p4s1,p4s2,p4s3,p4s4,
            p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20,p21,p22,
            p23,p24,p25,p26,p27,p28,p29,p30,p31,p32,p33,p34,p35,p36,p37,p38,p39,p40,p41,p42,
            p43,p44,p45,p46,p47,p48,p49,p50,p51,p52,p53,p54,p55,p56,p57,p58,p59,p60,p61,p62,
            p63,p64,p65,p66,p67,p68,p69,p70,p71,p72,p73,p74,p75,p76,p77,p78,p79,p80,p81,p82,
            p83,p84,p85,p86,p87,p88]

def marker_move(win, l_index, marker):
    list = positions()
    marker.move(win, list[l_index])

def game_winner(positions1, positions2, positions3, positions4, Player1, Player2, Player3, Player4):
    if positions1 == [73,74,75,76]:
        winner = Player1
    elif positions2 == [82,83,84,85]:
        winner = Player2
    elif positions3 == [91,92,93,94]:
        winner = Player3
    else:
        winner = Player4
    return winner
    

def congratulations(win, winner):
    rect = Rectangle(Point(-5,105),Point(105,-5))
    rect.setFill("white")
    rect.draw(win)
    win_text = Text(Point(50,50),"Congratulations {0}!".format(winner))
    win_text.setSize(36)
    win_text.draw(win)
    reset = Button(win, Point(15,15), 10, 7, "RESET")
    reset.activate()
    quit = Button(win, Point(85,15), 10, 7, "QUIT")
    quit.activate()
    for i in range(100):
        val = [randrange(256),randrange(256),randrange(256)]
        rect.setFill(color_rgb(val[0],val[1],val[2]))
        reset.textColor(color_rgb(val[0],val[1],val[2]))
        quit.textColor(color_rgb(val[0],val[1],val[2]))
        val2 = [255-val[0],255-val[1],255-val[2]]
        win_text.setFill(color_rgb(val2[0],val2[1],val2[2]))
        reset.buttonColor(color_rgb(val2[0],val2[1],val2[2]))
        quit.buttonColor(color_rgb(val2[0],val2[1],val2[2]))
    pt = win.getMouse()
    while not (reset.clicked(pt) or quit.clicked(pt)):
        pt = win.getMouse()
    if reset.clicked(pt):
        win.close()
        main()
    else:
        win.close()

def main():
    print("Clip 'Em 1.0 (May 13 2011, 05:57:48)")
    print("Copyright (c) 2011 Todrew Foundation.")
    print("All Rights Reserved.\n")
    print("WARNING! Those prone to epileptic seizures may")
    print("be at risk while playing this game.")
    print("Viewer discretion is advised.")
    win = makeGraphWin()
    printInstructions(win)
    p1, v1, p2, v2, p3, v3, p4, v4 = playerInfo(win)
    Player1, Player2, Player3, Player4 = playOrder(p1, v1, p2, v2, p3, v3, p4, v4)
    c1, c2, c3, c4 = playerColors(win, Player1, Player2, Player3, Player4)
    DrawBoard(win, Player1, Player2, Player3, Player4, c1, c2, c3, c4)
    m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12, m13, m14, m15, m16 = markers(win, c1, c2, c3, c4)
    positions1, positions2, positions3, positions4 = turn(win, Player1, Player2, Player3, Player4, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12, m13, m14, m15, m16)
    winner = game_winner(positions1, positions2, positions3, positions4, Player1, Player2, Player3, Player4)
    congratulations(win, winner)
 
main()
