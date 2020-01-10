#!/bin/python3
LOOP = 12
N = 6
m = [[j+1 for j in range(N)] for i in range(N)]
city = m
l0 = [l for l in range(4*N)]
l1 = [0,0,0,2,2,0,0,0,0,6,3,0,0,4,0,0,0,0,4,4,0,3,0,0]
limits = l1
log = []
needToCorrect = True
loop = 0
while needToCorrect:
    needToCorrect = False
    loop += 1
    for i in range(N):
        #local max (keyframe) coordinates
        if(limits[4*N-1-i]==0):
            limitL = -1
        else:
            limitL = limits[4*N-1-i]-1
        if(limits[N+i]==0):
            limitR = -2
        else:
            limitR = 6-limits[N+i]
        #print(limitL, limitR, sep=' - ')

        #limits
        if(limitL<0 and limitR<0):
            log.append(['all continue str',[i]])
            continue
        for j in range(N):
            if(limitL<0 and j<limitR-1):
                #j = limitR-1
                log.append(['zero L',[i,j]])
                continue
            if(limitR<0 and j>=limitL+1):
                log.append(['zero R',[i,j]])
                break
            if(j+1>=N):
                log.append(['last',[i,j]])
                break
            #change
            if((limitL>=0 and j<limitL and city[i][j]>city[i][j+1]) or
            (limitL>=0 and j==limitL and city[i][j]<city[i][j+1]) or
            (limitR>=0 and j==limitR-1 and city[i][j]>city[i][j+1]) or
            (limitR>=0 and j>=limitR and city[i][j]<city[i][j+1])):
                city[i][j],city[i][j+1] = city[i][j+1],city[i][j]
                log.append(['change'.upper(),[i,j],loop])
                needToCorrect = True
            else:
                log.append(['nothing',[i,j]])
        #print(loop,end='|')
        #if(loop>=LOOP): needToCorrect = False

#out
limits_orig = []
for i in range(N):
    limitL = limits[4*N-1-i]
    limitR = limits[N+i]
    limits_orig += [[limitL, limitR]]

print()
for i in range(6):
    print(limits_orig[i][0], end=' | ')
    for j in range(6):
        print(city[i][j], end=' ')
    print(' | '+str(limits_orig[i][1]))
    print()
if(False):
    for i in log:
        if(i[0]=='change'.upper() and i[2]<=5):
            print(i)
