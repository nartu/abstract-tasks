from turtle import Turtle, Screen
from math import pi, degrees, radians
from math import sin, cos, asin, acos

coord = [(0,0),(50,14),(67,37),(100,46),(140,68)]
coord2 = [(200,98),(204,160),(240,300),(250,25),(200,35)]
coord3 = [(200,98),(204,160)]
coordX = [(i[0]*4,i[1]) for i in coord]
coordCircle = [(30,60) for i in range(6)]
k = 30 # spiral
js = 1 # p = kj, j - radian step
n = 4 # steps
coordSpiral = [(js * i * k, degrees(js * i) % 360) for i in range(1,n)]
coord = coordSpiral
# coord = coord2

t = Turtle()
t.shape('triangle')
t.speed(10)

t.color('#81F7F3')
for c in coord:
    t.left(c[1])
    t.forward(c[0])
    t.home()

# first triangle
# t.speed(1)
# t.color('#04B404')
# c0 = coord[0]
# c1 = coord[1]
#
# O = c0[1] #ofset
# C = c1[1] - c0[1]
# ca = c0[0]
# bc = c1[0]
# cosC = cos(radians(C))
# ab = (ca ** 2 + bc ** 2 - 2*ca*bc*cosC) ** 0.5
# A = degrees(asin(bc * sin(radians(C)) / ab))
# A = 180 - A if cosC>=0 else A
# B = 180 - A - C
#
# t.left(O)
# t.forward(ca)
# t.left(180-A)
# t.forward(ab)
# t.left(180-B)
# t.forward(bc)

# triangles

t.home()
color = '#04B404'
for c in range(len(coord)-1):
    t.speed(1)
    color = f'#{int(color[1:], 16) + 50890*c:06x}'
    t.color(color)

    c0 = coord[c]
    c1 = coord[c+1]

    if c == 0: # ofset
        O = c0[1]
    else:
        O = 0
        t.left(180)
    C = c1[1] - c0[1]
    ca = c0[0]
    bc = c1[0]
    cosC = cos(radians(C))
    ab = (ca ** 2 + bc ** 2 - 2*ca*bc*cosC) ** 0.5
    A = degrees(asin(bc * sin(radians(C)) / ab))
    A = 180 - A if cosC>=0 else A
    B = 180 - A - C

    t.left(O)
    t.forward(ca)
    t.left(180-A)
    t.forward(ab)
    t.left(180-B)
    t.forward(bc)

# contour

t.home()
t.color('red')
t.pensize(2)
t.speed(1)
Bprev = 180

# first
t.left(coord[0][1])
t.forward(coord[0][0])

while False:
    for c in range(1, len(coord)-1):
        c0 = coord[c]
        c1 = coord[c+1]
        C = (c1[1] - c0[1]) % 360
        ca = c0[0]
        bc = c1[0]
        cosC = cos(radians(C))
        ab = (ca ** 2 + bc ** 2 - 2*ca*bc*cosC) ** 0.5
        A = degrees(asin(bc * sin(radians(C)) / ab))
        # Ap = A if cosC<=0 else 180 - A
        # A = 180 - A if cosC>=0 else A

        if c == 0:
            t.left(180 - A)
        else:
            P = A - (180 - Bprev)
            t.right(P)
        t.forward(ab)

        # Bprev = Ap - C
        Bprev = 180 - A - C

    # last
    # B = Bprev
    # t.left(180-B)
    # t.forward(bc)

Screen().mainloop()
