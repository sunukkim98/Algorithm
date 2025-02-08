import sys
input = sys.stdin.readline

N = int(input().strip())
k = N + 1
result = 0
for i in range(k):
    for j in range(i+1):
        result += i + j
print(result)