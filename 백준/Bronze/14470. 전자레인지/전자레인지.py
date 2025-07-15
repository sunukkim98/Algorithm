import sys
input = sys.stdin.readline

a = int(input().strip())
b = int(input().strip())
c = int(input().strip())
d = int(input().strip())
e = int(input().strip())

time = 0
if a < 0:
    time += abs(a) * c
    time += d
    time += b * e
else:
    time += (b - a) * e

print(time)
