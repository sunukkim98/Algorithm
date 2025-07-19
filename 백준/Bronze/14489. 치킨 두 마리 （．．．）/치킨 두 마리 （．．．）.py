import sys
input = sys.stdin.readline

a, b = map(int, input().split())
c = int(input().strip())

if a + b >= c * 2:
    print((a + b) - (c * 2))
else:
    print(a + b)
