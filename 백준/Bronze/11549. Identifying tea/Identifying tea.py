import sys
input = sys.stdin.readline

t = int(input().strip())
ans = list(map(int, input().split()))
cnt = 0
for a in ans:
    if a == t:
       cnt += 1
print(cnt)

