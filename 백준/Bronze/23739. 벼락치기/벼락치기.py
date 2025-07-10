import sys
input = sys.stdin.readline

n = int(input().strip())
cnt = 0
time = 30
for i in range(n):
    t = int(input().strip())
    if (t/2) <= time:
        cnt += 1
        if time - t > 0:
            time -= t
        else:
            time = 30
    else:
        time = 30
    # print(cnt)
    # print(time)
print(cnt)
