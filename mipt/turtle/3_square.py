import turtle

turtle.shape('square')
side = 100

turtle.speed(1)
turtle.right(0)
turtle.forward(side)
for i in range(3):
    turtle.left(90)
    turtle.forward(side)

turtle.mainloop()
