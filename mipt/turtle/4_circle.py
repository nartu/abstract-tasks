from turtle import Turtle, Screen

t = Turtle()
t.shape('circle')
t.speed(100)
side_l = 1
side_c = 360

for i in range(side_c):
    t.left(360/side_c)
    t.forward(side_l)

Screen().mainloop()
