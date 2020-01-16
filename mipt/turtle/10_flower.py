from turtle import Turtle, Screen
from math import pi, degrees, radians
from math import sin, cos, asin, acos

t = Turtle()

def circle(r = 50):
    edge = 60
    a = r * 2 * sin(radians(360 / (2 * edge)))
    A = 360 / edge
    # ofset x
    # Ox = (r + r * sin(radians((180 - A) / 2)))/2 if edge%2 == 1 else r
    # Ox = r
    # t.setheading(90)
    # t.penup()
    # t.goto(Ox,0)
    # t.right((A / 2))
    # t.pendown()
    for i in range(edge):
        t.left(A)
        t.forward(a)
t.speed(7)
n = 8
C = 360 / n
for i in range(n):
    circle()
    t.left(C)


Screen().mainloop()
