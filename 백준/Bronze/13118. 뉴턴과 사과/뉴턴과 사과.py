import sys
input = sys.stdin.readline

p = list(map(int, input().split()))
x, y, r = map(int, input().split())
flag = False
for pos in p:
    if pos == x:
        flag = True
        print(p.index(x) + 1)

if not flag:
    print(0)
