import sys
input = sys.stdin.readline

c, k, p = map(int, input().split())
total = 0
for i in range(1, c+1):
    total += (k * i) + (p * (i ** 2))
print(total)
