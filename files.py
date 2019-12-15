import os
import requests
f_in = "dataset_3378_3.txt"
f_out = "lesson_3.6.2.txt"
dir = "https://stepic.org/media/attachments/course67/3.6.3/"
pIn = os.path.join(".",f_in)
pOut = os.path.join(".",f_out)
with open(pIn, 'r') as file: #first
    link = file.readline().strip()
filename = requests.get(link).text
loop = True
c = 1
while loop:
    url = os.path.join(dir,filename)
    print(url)
    filename = requests.get(url).text.strip()
    print("\tFilename ("+str(c)+"): "+filename[:10])
    if(filename[:2]=="We"):
        loop = False
        with open(pOut, 'w') as file:
            file.write(filename)
        print('-'*25)
        print(filename)
    c += 1
