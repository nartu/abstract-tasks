from turtle import Turtle, Screen
from math import pi, degrees, radians

s = 10 # step
n = 24
ss = s
t = Turtle()
t.speed(5)

for i in range(n):
    t.forward(ss)
    t.left(90)
    ss += (i%2) * s


Screen().mainloop()
