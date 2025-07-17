import sys
input = sys.stdin.readline

k, n = map(int, input().split())

moves = list(map(int, input().split()))

cur = n
round = 0
for move in moves:
    if cur == 0:
        cur = n
    if cur - move >= 0:
        cur -= move
        if cur == 0:
            round += 1

print(round)
print(cur)
