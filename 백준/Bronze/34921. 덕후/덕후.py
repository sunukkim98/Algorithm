import sys

# next goal: Bronze 3

a, t = sys.stdin.readline().split()
a = int(a)
t = int(t)

val = 10 + 2 * (25 - a + t)
if val > 0:
    print(val)
else:
    print(0)
