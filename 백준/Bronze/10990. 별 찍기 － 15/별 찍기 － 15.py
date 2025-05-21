import sys
input = sys.stdin.readline

N = int(input().strip())
for i in range(1, N + 1):
    if i == 1:
        print(" " * (N - i) + "*" + " " * (i * 2 - 3))
    else:
        print(" " * (N - i) + "*" + " " * (i * 2 - 3) + "*")