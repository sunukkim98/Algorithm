import sys
input = sys.stdin.readline

y = int(input().strip())
m = int(input().strip())
old = m + (m - y)
print(old)
