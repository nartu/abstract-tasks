aS = 'abcd'
aC = '*d%#'
sS = 'abacabadaba'
sC = '#*%*d*%'

aS = input()
aC = input()
sS = input()
sC = input()

crypt = dict()
deCrypt = dict()
for i in range(len(aS)):
    crypt[aS[i]] = aC[i]
    deCrypt[aC[i]] = aS[i]
cryptStr = ''
for a in sS:
    cryptStr += crypt[a]
deCryptStr = ''
for a in sC:
    deCryptStr += deCrypt[a]

print(cryptStr)
print(deCryptStr)

'''
a,b,c,d=input(),input(),input(),input()
print(''.join(b[a.index(i)] for i in c))
print(''.join(a[b.index(i)] for i in d))
'''
