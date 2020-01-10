import os
f_in = "dataset_3363_4.txt"
f_out = "lesson_3.4.4.txt"
pIn = os.path.join(".",f_in)
pOut = os.path.join(".",f_out)
av = []
avA = [0 for i in range(3)]


'''txt =
Петров;85;92;78
Сидоров;100;88;94
Иванов;58;72;85
'''
#file = txt.strip().split('\n')

with open(pIn, 'r') as file:
    for line in file:
        buf = line.strip().split(';')
        del buf[0]
        for i in range(len(buf)): #common average sum
            buf[i] = int(buf[i])
            avA[i] += buf[i]
        av += [sum(buf)/len(buf)] #individul average sum

avALine = ''
for a in avA:
    avALine += str(a/len(av))+' '

#out
with open(pOut, 'w') as file:
    for a in av:
        file.write(str(a)+'\n')
    file.write(avALine)

print(av)
print(avALine)
