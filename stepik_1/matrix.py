#!/bin/python3

# put your python code here
m=[]
b=True
#ввод данных
while b:
    src = input()
    if(src=='end'): 
        b = False
        break
    m += [[int(j) for j in src.split()]]
#выходная матрица
out=m.copy()
for i in range(len(m)):
    for j in range(len(m[0])):
        #out[i][j] = -m[i][j]
        out[i][j] = ''
        for di in range(-1,2):
            for dj in range(-1,2):
                ai=(i+di)%len(m) #координаты соседей
                aj=(j+dj)%len(m[0])
                out[i][j] += str(ai)+' '+str(aj)+' | '
print(out[2][2])