import sys
input = sys.stdin.readline

# 다음 풀 문제: 실버 4

a, b, c, m = map(int, input().split())
tired = 0
work_h = 0
for i in range(24):
    if tired + a <= m:
        tired += a
        work_h += b
    else:
        tired -= c
        if tired < 0:
            tired = 0
print(work_h)
