import sys
input = sys.stdin.readline

n = int(input().strip())
times = []
for _ in range(n):
    a, b = map(int, input().split())
    if a <= b:
        times.append(b)
if len(times) == 0:
    print(-1)
else:
    print(min(times))
