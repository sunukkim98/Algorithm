import sys
input = sys.stdin.readline

n = int(input().strip())
for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print('*', end='')
    print()
