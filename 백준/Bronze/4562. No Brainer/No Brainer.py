import sys
input = sys.stdin.readline

n = int(input().strip())
for _ in range(n):
    x, y = map(int, input().split())
    if x < y:
        print("NO BRAINS")
    else:
        print("MMM BRAINS")
