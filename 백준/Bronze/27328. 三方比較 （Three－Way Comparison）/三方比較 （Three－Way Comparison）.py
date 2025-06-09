import sys
input = sys.stdin.readline

A = int(input().strip())
B = int(input().strip())
if A < B:
    print(-1)
elif A == B:
    print(0)
else:
    print(1)
