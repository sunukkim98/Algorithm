from sys import stdin as stdin

while True:
    a, b = map(int, stdin.readline().split())
    if a == 0 and b == 0:
        exit()
    if a > b:
        print('Yes')
    else:
        print('No')