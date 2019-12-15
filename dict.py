d = int(input())
dA = {input().lower() for i in range(d)}
l = int(input())
lA = [input().lower().split() for i in range(l)]
noDict = set()
for l in lA:
    for i in l:
        if(i not in dA and i not in noDict):
            noDict.add(i)
print(*noDict, sep='\n')


# формируем множество известных слов на основании построчного ввода
dic = {input().lower() for _ in range(int(input()))}

# заводим пустое множество для приема текста
wrd = set()

# т.к. текст построчно подается, а также в каждой строке несколько слов,
# то каждую строку превращаем во множество и добавляем в единое множество wrd
#для множеств это работает как присоединение, а в остальных случаях аналогично += и др.
#https://stackoverflow.com/questions/3929278/what-does-ior-do-in-python
for _ in range(int(input())):
    wrd |= {i.lower() for i in input().split()}

# на вывод отправляем результат вычитания словарного множества dic
# из текстового множества wrd; впереди ставим *, чтобы раскрыть поэлементно
print(*(wrd-dic), sep="\n")
print(*wrd.difference(dic), sep="\n")
