#test try except else finally

a = 0
try:
    print(a + 'a')
except TypeError as err:
    print(err)
    print('my text')
    print(err.__class__)
else:
    print('Nothing happens')
finally:
    print('TEST')

# print("{0:*^15}".format(1234567))
# text = 'hello'
# print(text[4:100])

# list = []
# for i in range(100):
#     list.append(lambda x, i = i : x+i)
# print(list[42](3))
