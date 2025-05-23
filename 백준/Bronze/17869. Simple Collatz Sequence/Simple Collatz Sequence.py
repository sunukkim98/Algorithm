import sys
input = sys.stdin.readline

n = int(input().strip())
cnt = 0
while n != 1:
    if n % 2 != 0:
        n += 1
        cnt += 1
    else:
        n /= 2
        cnt += 1
print(cnt)