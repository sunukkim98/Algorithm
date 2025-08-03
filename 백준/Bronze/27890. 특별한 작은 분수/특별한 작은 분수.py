import sys
input = sys.stdin.readline

x_0, n = map(int, input().split())
result = x_0
for _ in range(n):
    if result % 2 == 0:
        result = (result // 2) ^ 6
    else:
        result = (2 * result) ^ 6
print(result)
