import sys
input = sys.stdin.readline

N = input().strip()
a = int(N[0])
b = int(N[1])
if a == b:
    print(1)
else:
    print(0)
