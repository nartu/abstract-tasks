from turtle import Turtle, Screen
from math import pi, degrees, radians
from math import sin, cos, asin, acos, tan, atan

p1, p2 = (0,0),(10,100)

p = Turtle()
p.shape('triangle')


k = 10
js = 0.1 # p = kj, j - radian step
n = 250 # steps
j = js

#test
while False:
    t = Turtle()
    t.speed(10)
    t.color('#CDF7F3')
    for i in range(1,n):
        t.left(degrees(js))
        t.forward(js * i * k)
        t.goto(0,0)

p.color('red')
p.speed(5)
p.pensize(2)
for i in range(n):
    s = js * i * k
    F = degrees(js * i) % 360
    x = s * cos(radians(F))
    y = s * sin(radians(F))
    p.goto(x,y)


Screen().mainloop()
