from turtle import Turtle, Screen

FONT = ("Arial", 18, "normal")

def clickHandler(x, y):
    yertle.undo()  # unwrite previous coordinates
    yertle.write((x, y), align="center", font=FONT)

yertle = Turtle(visible=False)

yertle.write((0, 0), align="center", font=FONT)

screen = Screen()

screen.onscreenclick(clickHandler)

screen.mainloop()
