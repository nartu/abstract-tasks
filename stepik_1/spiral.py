#!/bin/python3

n = int(input())
#n = 6

m = [['-' for j in range(n)] for i in range(n)]
#e = n-1 #end of matrix
d = 1
for k in range(n):
    if(k<n):
        if(False):
            if(k%2==0):
                for i in range(0,n,1):
                    for j in range(0,n,1):
                        b = k//2 #begin of matrix
                        e = n-1-b #end of matrix
                        if((i==b and j>=b and j<=e) or (j==e and i>=b and i<=e)):
                            m[i][j] = d
                            d += 1
                        #else: m[i][j] = e
            elif(k%2==1):
                for i in range(n-1,-1,-1):
                    for j in range(n-1,-1,-1):
                        b = k//2 #end of matrix
                        e = n-1-b #begin of matrix
                        if((i==e and j>=b and j<e) or (j==b and i>b and i<=e)):
                            m[i][j] = d
                            d += 1
    if(True):
        if(k%2==0): gb,ge,gs = 0,n,1 #direction of reading
        else:  gb,ge,gs = n-1,-1,-1
        b = k//2 #begin of matrix
        e = n-1-b #end of matrix
        for i in range(gb,ge,gs):
            for j in range(gb,ge,gs):
                if((j>=b and j<=e-k%2) and (i>=b+k%2 and i<=e)):
                    if(k%2==1): b,e = e,b
                    if(i==b or j==e):
                        m[i][j] = d
                        d += 1
                    if(k%2==1): b,e = e,b
for i in range(n):
    for j in range(n):
        print(m[i][j], end=' ')
    print()
