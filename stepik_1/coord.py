n = int(input())
c = [input().split() for _ in range(n)]
x,y = 0,0
for i in c:
    co = int(i[1])
    if(i[0]=='север'):
        y += co
    elif(i[0]=='юг'):
        y -= co
    elif(i[0]=='восток'):
        x += co
    elif(i[0]=='запад'):
        x -= co
print(x,y,sep=' ')
