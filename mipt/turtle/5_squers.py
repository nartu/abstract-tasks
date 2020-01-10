from turtle import Turtle, Screen

t = Turtle()
t.shape('triangle')
t.speed(4)
side_l = 50
side_c = 4
f_num = 4
offset = 10

for f in range(f_num):
    for i in range(side_c):
        t.right(360/side_c)
        t.forward(side_l)
    t.penup()
    t.left(90)
    t.forward(offset)
    t.right(90)
    t.forward(offset)
    # t.right(180)
    t.pendown()
    side_l = side_l + 2 * offset


Screen().mainloop()
