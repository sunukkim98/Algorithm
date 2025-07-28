import sys
input = sys.stdin.readline

n = int(input().strip())
cnt = 0
for _ in range(n):
    d_i = input().strip()
    d = int(d_i[2:])
    if d <= 90:
        cnt += 1
print(cnt)
