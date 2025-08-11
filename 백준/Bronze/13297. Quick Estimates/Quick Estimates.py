import sys
input = sys.stdin.readline

n = int(input().strip())
for _ in range(n):
    line = input().strip()
    print(len(line))
