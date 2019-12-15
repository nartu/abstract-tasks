#!/bin/python3
import copy
loop = 0
LOOP = 25
N = 6
cityMax = [[0 for j in range(N)] for i in range(N)]
city = [[j+1 for j in range(N)] for i in range(N)]
l0 = [l for l in range(4*N)]
l1 = [0,0,0,2,2,0,0,0,0,6,3,0,0,4,0,0,0,0,4,4,0,3,0,0]
limits = l1
log = []
needToCorrect = True
loop = 0

#function
def hardPosition(I,J):
    if(N in [lm[0][I],lm[1][I],lm[2][J],lm[3][J]]):
        return True
    if((lm[0][I]==1 and J==0) or (lm[1][I]==1 and J==N-1) or
    (lm[2][J]==1 and I==0) or (lm[3][J]==1 and I==N-1)):
        return True
    if(lm[0][I]+lm[1][I]==7 and cityMax[I][J]==N):
        return True
    if(lm[2][J]+lm[3][J]==7 and cityMax[I][J]==N):
        return True
    return False
def unique(I,J):
    for j in range(N):
        if(j!=J and city[I][j] == city[I][J]):
             return False
    for i in range(N):
        if(i!=I and city[i][J] == city[I][J]):
            return False
    return True
def countInCol(I,J,M=cityMax):
    c=0
    for i in range(N):
        if(i!=I and M[i][J] == M[I][J]):
            c+=1
    return c
def countInRowD(I,J,M=cityMax):
    out = [[],[]]
    out[0]=0
    for j in range(N):
        if(M[i][J] == D):
            out[0]+=1
            out[1]+=[i] #target coordinate of D in row
    return out
def countInColD(J,D,M=cityMax):
    out = [[],[]]
    out[0]=0
    for i in range(N):
        if(M[i][J] == D):
            out[0]+=1
            out[1]+=[i] #target coordinate of D in column
    return out
def countInRowD(I,D,M=cityMax):
    out = [[],[]]
    out[0]=0
    for j in range(N):
        if(M[I][j] == D):
            out[0]+=1
            out[1]+=[j] #target coordinate of D in row
    return out


#limits massive
lm = [[] for i in range(4)]
for i in range(N):
    limitL = limits[4*N-1-i]
    limitR = limits[N+i]
    limitT = limits[i]
    limitB = limits[3*N-1-i]
    lm[0].append(limitL)
    lm[1].append(limitR)
    lm[2].append(limitT)
    lm[3].append(limitB)

#maximum
for i in range(N):
    for j in range(N):
        maxL = (N+1)-lm[0][i]+j
        maxR = (N+1)-lm[1][i]+(N-1-j)
        maxT = (N+1)-lm[2][j]+i
        maxB = (N+1)-lm[3][j]+(N-1-i)
        max = min(maxL,maxR,maxT,maxB)
        if(max<=6):
            cityMax[i][j] = max


#City prepare
def firstLimits(direction,i):
    mi = 0 #maximum of row Left
    mic = 0 #count of steps to maximum of row
    #b,e,s begin, end, step
    loop = 0
    if(direction=='Left'):
        direction = 0
        b,e,s = 0,N,1
        delta = 1
        edge = 0
    elif(direction=='Right'):
        direction = 1
        b,e,s = N-1,-1,-1
        delta = -1
        edge = N-1
    if(lm[direction][i] != 0):
        while(mi!=N or mic!=lm[direction][i]):
            print(i)
            loop += 1
            for j in range(b,e,s):
                if(mic==lm[direction][i]-1 and city[i][j]==N):
                    mi = city[i][j]
                    mic += 1
                elif(mic==lm[direction][i]-1 and city[i][j]>mi and mi<N):
                    city[i][city[i].index(6)],city[i][j] = city[i][j],city[i][city[i].index(6)]
                    mi = city[i][j]
                    mic += 1
                elif(mi==N and mic<lm[direction][i]-1):
                    city[i][j+delta],city[i][j] = city[i][j],city[i][j+delta]
                    mi = city[i][j]
                    mic += 1
                elif(mic==0 or city[i][j-delta]<city[i][j]):
                    mi = city[i][j]
                    mic += 1
            if(loop>=36):
                print(mi)
                print(mic)
                break
            return True

#First step
for i in range(0,N):
    firstLimits('Right',i)






'''
for i in range(N):
    for j in range(N):
        city[i][j] = cityMax[i][j]

while needToCorrect:
    needToCorrect = False
    loop += 1
    for i in range(N):
        for j in range(N):
            if(not hardPosition(i,j) and not unique(i,j)):
                for d in range(cityMax[i][j],0,-1):
                    city[i][j] = d
                    if(unique(i,j)):
                        break

                needToCorrect = True
    if(loop>36):
        needToCorrect = False
'''
#out

print()
for j in range(2):
    print(' ', end=' ')
for j in range(N):
    print(limits[j], end=' ')
print()
for j in range(N+4):
    if(j<=1 or j>=N+4-3):
        print(' ', end=' ')
    else:
        print('_', end='_')
print()
for i in range(6):
    print(lm[0][i], end=' | ')
    for j in range(6):
        print(city[i][j], end=' ')
    print(' | '+str(lm[1][i]))


for j in range(N+4):
    if(j<=1 or j>=N+4-3):
        print(' ', end=' ')
    else:
        print('_', end='_')
print()
for j in range(19,11,-1):
    if(j>=18):
        print(' ', end=' ')
    else:
        print(limits[j], end=' ')
print()

#Print cityMax
print()
for j in range(2):
    print(' ', end=' ')
for j in range(N):
    print(lm[2][j], end=' ')
print()
for j in range(N+4):
    if(j<=1 or j>=N+4-3):
        print(' ', end=' ')
    else:
        print('_', end='_')
print()
for i in range(N):
    print(lm[0][i], end=' | ')
    for j in range(N):
        print(cityMax[i][j], end=' ')
    print(' | '+str(lm[1][i]))
for j in range(N+4):
    if(j<=1 or j>=N+4-3):
        print(' ', end=' ')
    else:
        print('_', end='_')
print()
for j in range(2):
    print(' ', end=' ')
for j in range(N):
    print(lm[3][j], end=' ')
print()

#print(cityMax)
#print(city)

if(False):
    for i in log:
        if(i[0]=='change'.upper() and i[2]<=5):
            print(i)
if(False):
    for i in log:
        print(i)
