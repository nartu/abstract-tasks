from turtle import Turtle, Screen
from math import pi, degrees, radians
from math import sin, cos, asin, acos

coord = [(0,0),(50,14),(67,37),(100,46),(140,68),(200,98)]
coordX = [(i[0]*4,i[1]) for i in coord]

t = Turtle()
text = Turtle()

t.shape('triangle')
t.speed(10)
t.color('#AE00FF')

text.penup()
text.shape('classic')
text.goto(150,100)
text.speed(10)

k = 60
js = 0.5 # p = kj, j - radian step
n = 4 # steps
j = js

for i in range(n):
    t.left(degrees(js))
    t.forward(k * js * i)
    t.goto(0,0)
    text.clear()
    text.write(k * js * i, font=("Arial", 20, "normal"))

t.home()
t.color('red')
t.pensize(2)
t.speed(5)
Bprev = 0

# C = degrees(js)
# ca = k * js
# bc = k * js * 2
# cosC = cos(js)
# ab = (ca ** 2 + bc ** 2 - 2*ca*bc*cosC) ** 0.5
# A = degrees(asin(bc * sin(js) / ab))
# A = A if cosC<0 else 180 - A
#
# t.left(C)
# t.forward(ca)
#
# t.left(180 - A)
# t.forward(ab)


# text.clear()
# text.write('A: {}, \n, ab: {}, \n, ca: {}'.format(t.heading(),ab,ca), font=("Arial", 20, "normal"))

#
# t.left(180 - A)
# t.forward(ab)

# if i == 0:
#     t.left(180 - A)
# else:
#     P = A - (180 - Bprev)
#     t.right(P)
# t.forward(ab)

# Bprev = Ap - C
# Bprev = 180 - A - C

Screen().mainloop()
