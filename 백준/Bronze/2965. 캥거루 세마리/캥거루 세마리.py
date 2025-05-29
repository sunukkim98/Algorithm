import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())
gap1 = B - A
gap2 = C - B
if gap1 > gap2:
    print(gap1 - 1)
else:
    print(gap2 - 1)