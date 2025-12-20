import sys

# input
n, w, h, l = map(int, sys.stdin.readline().split())

temp = (w // l) * (h // l)
if temp > n:
    print(n)
else:
    print(temp)
