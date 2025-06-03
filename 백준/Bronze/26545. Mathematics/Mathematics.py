import sys
input = sys.stdin.readline

n = int(input().strip())
result = 0
for _ in range(n):
    result += int(input().strip())
print(result)
