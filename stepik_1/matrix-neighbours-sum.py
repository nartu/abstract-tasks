# put your python code here
m=[]
b=True
shifts = [[-1,0],[1,0],[0,-1],[0,1]]
#ввод данных
while b:
    src = input()
    if(src=='end'):
        b = False
        break
    m += [[int(j) for j in src.split()]]
#выходная матрица
y = len(m)
x = len(m[0])
out = [[0 for j in range(x)] for i in range(y)]
for i in range(y):
    for j in range(x):
        for s in shifts:
            si = (i+s[0])%y
            sj = (j+s[1])%x
            #out[i][j] += str(si)+'-'+str(sj)+'|' #отладка, координаты соседей
            out[i][j] += m[si][sj]
for i in range(y):
    for j in range(x):
        print(out[i][j],end=' ')
    print()
