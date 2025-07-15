import sys
input = sys.stdin.readline

n = int(input().strip())
for _ in range(n):
    length = int(input().strip())
    for i in range(length):
        print("=", end='')
    print()
