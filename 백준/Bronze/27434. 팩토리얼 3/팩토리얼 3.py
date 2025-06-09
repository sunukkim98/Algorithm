import sys
input = sys.stdin.readline

N = int(input().strip())
if N == 0:
    print(1)
    exit()
result = 1
for i in range(1, N+1):
    result *= i
print(result)
