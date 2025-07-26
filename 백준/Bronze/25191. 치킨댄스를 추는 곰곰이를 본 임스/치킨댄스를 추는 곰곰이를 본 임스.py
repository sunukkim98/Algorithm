import sys
input = sys.stdin.readline

n = int(input().strip())
a, b = map(int, input().split())
candidate = a // 2 + (b)
# print(candidate)
if candidate > n:
    print(n)
else:
    print(candidate)
