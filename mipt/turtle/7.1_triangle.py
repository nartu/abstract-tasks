from turtle import Turtle, Screen
from math import pi, degrees, radians
from math import sin, cos, asin, acos

t = Turtle()
t.shape('triangle')
t.speed(5)

# Angles
O = 15 # ofset
A = 10
B = 50
C = 180 - (A + B)
# Sides
ab = 50
ca = ab * sin(radians(B)) / sin(radians(C))
bc = (ca ** 2 + ab ** 2 - 2*ca*ab*cos(radians(A))) ** 0.5

t.color('green')
t.left(O)
t.forward(ca)
t.left(180-A)
t.forward(ab)
t.left(180-B)
t.forward(bc)


Screen().mainloop()
