from turtle import Turtle, Screen
from math import pi, degrees, radians
from math import sin, cos, asin, acos

n = 4
rb = 50
rs = 30
edge = 3

t = Turtle()


def polygon(edge,r):
    a = r * 2 * sin(radians(360 / (2 * edge)))
    A = 360 / edge
    # ofset x
    # Ox = (r + r * sin(radians((180 - A) / 2)))/2 if edge%2 == 1 else r
    Ox = r
    t.setheading(90)
    t.penup()
    t.goto(Ox,0)
    t.right((A / 2))
    t.pendown()
    for i in range(edge):
        t.left(A)
        t.forward(a)

os = Turtle()
os.color('yellow')
os.speed(6)
os.goto(-100,0)
os.goto(100,0)
os.penup()
os.goto(0,-100)
os.pendown()
os.goto(0,100)

t.speed(4)

for i in range(n):
    if(i % 2 == 1):
        t.color('blue')
    else:
        t.color('black')
    polygon(edge,rb)
    edge += 1
    rb += rs

Screen().mainloop()
