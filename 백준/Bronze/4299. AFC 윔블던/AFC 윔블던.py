import sys
input = sys.stdin.readline

summation, subtraction = map(int, input().split())
x = (summation + subtraction)
y = (summation - subtraction)
if x % 2 != 0 or y % 2 != 0 or y < 0:
    print(-1)
else:
    x //= 2; y //= 2
    if x < y: x,y = y,x
    print(x, y)
