import os
f_in = "dataset_3380_5.txt"
pIn = os.path.join(".",f_in)
stat_src = {i+1:[0,0] for i in range(11)}
with open(pIn, 'r') as file:
    for line in file:
        s = line.strip().split('\t')
        stat_src[int(s[0])][0] += int(s[2])
        stat_src[int(s[0])][1] += 1
for k,v in stat_src.items():
    r = float(v[0]/v[1]) if v[1]>0 else '-'
    print(k,r,sep=' ')

#print(stat_src)
#[print('{} {}'.format(i+1, float(stat_src[i+1][0]/stat_src[i+1][1])), sep=' ') for i in range(11)]
