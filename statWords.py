import os
f_in = "dataset_3363_3.txt"
f_out = "lesson_3.4.txt"
pIn = os.path.join(".",f_in)
pOut = os.path.join(".",f_out)
stat = dict()
with open(pIn, 'r') as file:
    for line in file:
        line = line.strip()
        #line = 'abc a bCd bC AbC BC BCD bcd ABC'
        buf = line.lower().split()
        for w in buf:
            if w in stat:
                stat[w] += 1
            else:
                stat[w] = 1
max =  max(stat.values())
maxs = [key for key, value in stat.items() if value == max]
maxKey = min(maxs)


#print(stat)
#print(max)
print(maxKey, max, sep=' ')
