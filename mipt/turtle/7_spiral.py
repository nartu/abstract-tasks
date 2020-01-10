from turtle import Turtle, Screen
from math import pi, degrees, radians
from math import sin, cos, asin, acos

t = Turtle()
t.shape('turtle')
t.speed(10)

k = 60
js = 0.5 # p = kj, j - radian step
n = 4 # steps
j = js


for i in range(n):
    t.color('yellow')
    t.left(degrees(js))
    t.forward(k*j)
    t.penup()
    t.backward(k*j)
    t.pendown()
    j += js
    print('j-rad: {}, j-d: {}, p: {}'.format(j,degrees(j),k*j))
t.home()
t.speed(1)
t.color('blue')
# a = k*js
# b = k*(js+js)
# c = (a**2 + b**2 - 2*a*b*cos(js)) ** 0.5
# jl = asin(b * sin(js) / c)
# R = radians(180)
# # jb = R - (R -((R-jl) + js))
# jb = R - jl + js
# t.left(degrees(js))
# t.forward(a)
# t.left(degrees(jl))
# t.forward(c)
# t.left(degrees(jb))
# t.forward(b)
# print(degrees(jb), degrees(jl), sep='   ')

j = js
jl = js
a = k*js
b = k*(js+js)
c = k * j
jb = 0
R = radians(180)
for i in range(n):
    t.speed(1)
    t.color('blue')
    t.left(degrees(jl))
    t.forward(c)

    a = k*j
    b = k*(j+js)
    c = (a**2 + b**2 - 2*a*b*cos(js)) ** 0.5
    jl = asin(b * sin(js) / c)
    jb = R - jl + js
    if i>1: jl = R - jb -jl
    j += js
    print('c: {}, jl: {}'.format(c,degrees(jl)))

Screen().mainloop()
