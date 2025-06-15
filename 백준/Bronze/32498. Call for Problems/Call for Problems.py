import sys
input = sys.stdin.readline

n = int(input().strip())
cnt = 0
for i in range(n):
    candidate = int(input().strip())
    if candidate % 2 != 0:
        cnt += 1
print(cnt)
