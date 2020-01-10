#from sys import argv as my_argv
import sys
for i in range(1,len(sys.argv)):
    print(sys.argv[i], end=' ')
print()
print(*sys.argv[1:])
print(*__import__("sys").argv[1:])
[print(i, end=' ') for i in sys.argv[1:]]
a=(sys.argv)
print(*a[1:])
for i in sys.argv[1:]:
    print(i, end=' ')
[print(c) for c in sys.argv[1:]]
