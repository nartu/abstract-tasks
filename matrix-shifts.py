#Source
x = 8
y = 11
shifts = [[-1,0],[1,0],[0,-1],[0,1]]
cell = [0,0] #target cell
border = False #consider borders of the matrix
#Body
m = [[0 for j in range(x)] for i in range(y)]
neighbours = []
m[cell[0]][cell[1]] = 2
if(border):
    for s in shifts:
        mi = (cell[0]+s[0]) #whitch row
        mj = (cell[1]+s[1]) #whitch column
        if(0<=mi<y and 0<=mj<x):
            neighbours += [[mi,mj]]
            m[mi][mj] = 1
        else:
            neighbours += [[mi,mj]]
else:
    for s in shifts:
        mi = (cell[0]+s[0])%y #whitch row
        mj = (cell[1]+s[1])%x #whitch column
        neighbours += [[mi,mj]]
        m[mi][mj] = 1
#Print
print(cell)
print(shifts)
print(neighbours)
out = m
for i in range(len(out)):
    for j in range(len(out[0])):
        print(out[i][j],end=' ')
    print()
