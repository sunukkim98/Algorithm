import sys
input = sys.stdin.readline

m = int(input().strip())
idx = 1
for _ in range(m):
    x, y = map(int, input().split())
    if y == idx:
        idx = x
    elif x == idx:
        idx = y
print(idx)
