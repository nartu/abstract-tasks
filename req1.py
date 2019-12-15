import os
import requests
f_in = "dataset_3378_2.txt"
f_out = "lesson_3.6.1.txt"
pIn = os.path.join(".",f_in)
pOut = os.path.join(".",f_out)
with open(pIn, 'r') as file:
    link = file.readline().strip()
r = requests.get(link)
tAr = r.text.splitlines()
cStr = len(tAr)
with open(pOut, 'w') as file:
    file.write(str(cStr))
print(cStr)
