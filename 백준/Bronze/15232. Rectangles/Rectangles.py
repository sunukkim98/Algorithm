import sys

r = int(sys.stdin.readline().strip())
c = int(sys.stdin.readline().strip())

for i in range(r):
    for j in range(c):
        print('*',end='')
    print()