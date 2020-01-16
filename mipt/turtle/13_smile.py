from turtle import Turtle, Screen
from math import pi, degrees, radians
from math import sin, cos, asin, acos

def os(ray=100):
    os = Turtle()
    os.color('red')
    os.speed(10)
    os.goto(-ray,0)
    os.goto(ray,0)
    os.penup()
    os.goto(0,-ray)
    os.pendown()
    os.goto(0,ray)

t = Turtle()
t.speed(10)

def arc(f='arc',r=50,coord=(0,0),direction=90):
    edge = 26
    a = r * 2 * sin(radians(360 / (2 * edge)))
    A = 360 / edge
    he = int(edge / 2) if f=='arc' else edge
    Ox = sin(radians(direction))*r + coord[0]
    Oy = coord[1]
    t.setheading(direction)
    t.right((A/2))
    # t.left(90)
    t.penup()
    t.goto(Ox,Oy)
    t.pendown()
    for i in range(he):
        t.left(A)
        t.forward(a)
t.home()

n = 3

t.color('black','yellow')
t.begin_fill()
arc('circle',100)
t.end_fill()
t.color('black','blue')
t.begin_fill()
arc('circle',10,coord=(-40,30))
t.end_fill()
t.begin_fill()
arc('circle',10,coord=(40,30))
t.end_fill()
t.pensize(6)
t.penup()
t.goto(0,30)
t.pendown()
t.goto(0,-20)
t.penup()

t.color('red')
arc('arc',30,(0,-40),270)

# os()


Screen().mainloop()
