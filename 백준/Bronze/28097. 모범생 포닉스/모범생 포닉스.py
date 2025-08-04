import sys
input = sys.stdin.readline

n = int(input().strip())
times = list(map(int, input().split()))

if n > 1:
    res = sum(times) + (8 * (n - 1))
else:
    res = sum(times)

days = res // 24
time = res % 24
print(days, time)
