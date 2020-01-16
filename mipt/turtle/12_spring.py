from turtle import Turtle, Screen
from math import pi, degrees, radians
from math import sin, cos, asin, acos


t = Turtle()
t.speed(10)

def arc(r=50,coord=(0,0)):
    edge = 60
    a = r * 2 * sin(radians(360 / (2 * edge)))
    A = 360 / edge
    he = int(edge / 2)
    Ox = -r + coord[0]
    Oy = coord[1]
    # t.left(90)
    # t.penup()
    # t.goto(Ox,Oy)
    # t.pendown()
    for i in range(he):
        t.right(A)
        t.forward(a)
t.home()
t.penup()
t.goto(-250,0)
t.pendown()
n = 3
t.left(90)
for i in range(n):
    arc()
    if i<n-1: arc(10)

Screen().mainloop()
