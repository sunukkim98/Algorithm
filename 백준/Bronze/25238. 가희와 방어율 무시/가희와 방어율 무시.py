import sys
input = sys.stdin.readline

a, b = map(int, input().split())
temp = a - (a * (b/100))
if temp >= 100:
    print(0)
else:
    print(1)
