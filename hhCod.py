#!/bin/python3
input = input()
remember = []
for d in range(len(input)):
    remember.append(int(input[d]))

codpanel = [[(j+1)+3*i for j in range(3)] for i in range(3)]
codpanel += [[-1,0,-1]]
maybeMask = [[0,0],[-1,0],[1,0],[0,-1],[0,1]]

rXYnative = []
for r in remember:
    if(r==0):
        rXY = [3,1]
    else:
        rXY = []
        rXY += [(r-1)//3]
        rXY += [codpanel[rXY[0]].index(r)]
    rXYnative += [rXY]

maybePool = []
for xy in rXYnative:
    maybePool += [[]]
    for shift in maybeMask:
        codY = xy[0]+shift[0]
        codX = xy[1]+shift[1]
        if(0<=codX<3 and 0<=codY<4 and codpanel[codY][codX]>=0):
            maybePool[len(maybePool)-1] += [codpanel[codY][codX]]

passPool = ['']
for i in range(len(maybePool)-1,-1,-1):
    t = []
    for d in maybePool[i]:
        for j in passPool:
            t.append(str(d)+str(j))
    passPool = t
passPool.sort()

#out
for i in range(len(passPool)-1):
    print(passPool[i], end=', ')
print(passPool[len(passPool)-1])
