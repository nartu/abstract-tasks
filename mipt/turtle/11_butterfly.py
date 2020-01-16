from turtle import Turtle, Screen
from math import pi, degrees, radians
from math import sin, cos, asin, acos

t = Turtle()
t.speed(10)

def circle(r = 50):
    edge = 60
    a = r * 2 * sin(radians(360 / (2 * edge)))
    A = 360 / edge
    for i in range(edge):
        t.left(A)
        t.forward(a)
r = 50
t.left(90)
for i in range(8):
    circle(r)
    t.right(180)
    r += i%2 * 20

Screen().mainloop()
