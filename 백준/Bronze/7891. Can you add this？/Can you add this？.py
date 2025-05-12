import sys

input = sys.stdin.readline

T = int(input().strip())
for i in range(T):
    x, y = map(int, input().split())
    print(x + y)