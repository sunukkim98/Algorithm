import sys
input = sys.stdin.readline

total = int(input().strip())
known = 0
for _ in range(9):
    known += int(input().strip())
print(total - known)
