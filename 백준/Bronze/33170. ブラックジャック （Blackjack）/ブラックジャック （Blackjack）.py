import sys
input = sys.stdin.readline

a = int(input().strip())
b = int(input().strip())
c = int(input().strip())
if a + b + c <= 21:
    print(1)
else:
    print(0)
