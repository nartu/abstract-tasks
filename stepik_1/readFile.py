import os
f_in = "dataset_3363_2.txt"
f_out = "lesson_3.4.txt"
pIn = os.path.join(".",f_in)
pOut = os.path.join(".",f_out)
ds = [str(i) for i in range(10)]
res = '' #result
with open(pIn, 'r') as file:
    for line in file:
        line = line.strip()
        lS = ''
        lD = ''
        endLine = len(line)-1
        c = 0
        for s in line:
            if((s not in ds and len(lS)>0 and len(lD)>0) or (c == endLine)):
                if(c == endLine):
                    lD += s
                res += lS * int(lD)
                #res += lS + lD
                lS = s
                lD = ''
            elif(s in ds):
                lD += s
            else:
                lS += s
            c += 1
#out
with open(pOut, 'w') as file:
    file.write(res)
#print(res)
