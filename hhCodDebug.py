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

tmp = ['']
#maybePool = [[1,2,3],[3,4,5],[5,6,7]]
for i in range(len(maybePool)-1,-1,-1):
    t = []
    for d in maybePool[i]:
        #t += ['t'+str(d)]
        for j in tmp:
            t.append(str(d)+str(j))
    tmp = t
    print(i)
    print(t)
    print(tmp)
    print(len(tmp))
#out
for i in range(4):
    for j in range(3):
        print(codpanel[i][j], end=' ')
    print()
print('-'*10)
print('',end='remember: ')
print(remember)
print('',end='coordinates: ')
print(rXYnative)
print('',end='maybePool: ')
print(maybePool)
print('',end='tmp: ')
print(t)
print(sorted(tmp))
