from turtle import Turtle, Screen

t = Turtle()
t.shape('turtle')
t.speed(4)

size = 50
n = 12

for i in range(n):
    t.left(360/n)
    t.forward(size)
    t.penup()
    t.backward(size)
    t.pendown()

Screen().mainloop()
