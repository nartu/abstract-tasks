#!/bin/python3
import copy
loop = 0
LOOP = 25
N = 6
cityMax = [[0 for j in range(N)] for i in range(N)]
city = [[0 for j in range(N)] for i in range(N)]
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
print(cityMax)
#correct maximum
for l in range(4):
    lmt = lm[l]
    if(l==0):
        for i in range(N): #list of limits left
            if(lmt[i] != 0):
                max_local = cityMax[i][0]
                max_count = 1
                for j in range(1,N):
                    print(str(i)+str(j)+' - c:'+str(max_count)+' - m:'+str(max_local))
                    if(cityMax[i][j] == N and max_count == lmt[i]-1):
                        break
                    elif(cityMax[i][j] > max_local):
                        max_local = cityMax[i][j]
                        max_count += 1
                    elif(cityMax[i][j] < max_local and cityMax[i][j] == 0): #can be if out of limit only
                        cityMax[i][j] = max_local+1
                        max_count += 1
                    elif(cityMax[i][j] < max_local and not hardPosition(i,j)):
                        print('!')
                        cityMax[i][j] -= 1
    elif(l==1):
        for i in range(N): #list of limits right
            if(lmt[i] != 0):
                max_local = cityMax[i][N-1]
                max_count = 1
                for j in range(N-2,-1,-1):
                    if(cityMax[i][j] == N and max_count == lmt[i]-1):
                        break
                    elif(cityMax[i][j] > max_local):
                        max_local = cityMax[i][j]
                        max_count += 1
                    elif(cityMax[i][j] < max_local and cityMax[i][j] == 0): #can be if out of limit only
                        cityMax[i][j] = max_local+1
                        max_count += 1
                    elif(cityMax[i][j] < max_local and not hardPosition(i,j-1)):
                        cityMax[i][j-1] -= 1
    elif(l==2):
        for j in range(N): #list of limits top
            if(lmt[i] != 0):
                max_local = cityMax[i][0]
                max_count = 1
                for j in range(1,N):
                    print(str(i)+str(j)+' - c:'+str(max_count)+' - m:'+str(max_local))
                    if(cityMax[i][j] == N and max_count == lmt[j]-1):
                        break
                    elif(cityMax[i][j] > max_local):
                        max_local = cityMax[i][j]
                        max_count += 1
                    elif(cityMax[i][j] < max_local and cityMax[i][j] == 0): #can be if out of limit only
                        cityMax[i][j] = max_local+1
                        max_count += 1
                    elif(cityMax[i][j] < max_local and not hardPosition(i+1,j)):
                        print('!')
                        cityMax[i+1][j] -= 1
    elif(l==3): #list of limits bottom
        for j in range(N):
            if(lmt[j] != 0):
                max_local = cityMax[N-1][j]
                max_count = 1
                for i in range(N-2,-1,-1):
                    print (max_count)
                    if(cityMax[i][j] == N and max_count == lm[3][j]-1):
                        break
                    elif(cityMax[i][j] > max_local):
                        max_local = cityMax[i][j]
                        max_count += 1
                    elif(cityMax[i][j] < max_local and cityMax[i][j] == 0): #can be if out of limit only
                        cityMax[i][j] = max_local+1
                        max_count += 1
                    elif(cityMax[i][j] < max_local and not hardPosition(i-1,j)):
                        cityMax[i-1][j] -= 1

        #lm[0][i] and j<lm[0][i]-1 and cityMax[i][j]>=cityMax[i][j+1]
        #lm[1][i] and j>N-lm[1][i] and cityMax[i][j]>=cityMax[i][j-1]
        #lm[2][j] and i<lm[2][j]-1 and cityMax[i][j]>=cityMax[i+1][j]

        #if(lm[3][j]>0 and i>N-lm[3][j] and cityMax[i][j]==cityMax[i-1][j]):
            #cityMax[i][j] = cityMax[i][j]

#City prepare

#Hard Position
for i in range(N):
    for j in range(N):
        if(hardPosition(i,j)):
            city[i][j] = cityMax[i][j]
#First step
for d in range(6,7):
    for i in range(0,N):
        dPlace = -1
        im = N #minumum of count in J col
        if(countInRowD(i,d)[0]>0):
            for j in countInRowD(i,d)[1]:
                imj = countInColD(j,d,city)[0] + countInColD(j,d)[0] #past + future
                if(hardPosition(i,j)):
                    dPlace = j
                    break
                elif(imj<=im):
                    im = imj
                    dPlace = j
        if(0 in cityMax[i]):
            log += ['d='+str(d)+' looking for 0 in cityMax i'+str(i)]
            for j in range(N):
                log += ['d='+str(d)+' test j'+str(j)]
                imj = countInColD(j,d,city)[0] + countInColD(j,d)[0] #past + future
                if(hardPosition(i,j)):
                    dPlace = j
                    break
                if(city[i][j]==0 and cityMax[i][j]==0 and imj<=im):
                    im = imj
                    dPlace = j
                    log += ['d='+str(d)+' found 0 j'+str(j)+' im='+str(im)+' dPlace='+str(dPlace)]
        if(dPlace>=0):
            city[i][dPlace] = d
            log += ['CHANGE city:'+str(i)+'-'+str(dPlace)+' = '+str(d)]



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
