import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
import math

# 다음 풀 문제: 실버 3

# 1072번 게임

# 각 줄에 정수 X와 Y가 주어진다.
x, y = map(int, input().split())
start = (100 * y) // x
left = 0
right = x
res = x

if start >= 99:
    print(-1)
else:
    while left <= right:
        mid = (left + right) // 2
        if (100 * (y + mid)) // (x + mid) > start:
            res = mid
            right = mid - 1
        else:
            left = mid + 1
    print(res)
