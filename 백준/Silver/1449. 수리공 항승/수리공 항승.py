import sys
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline
# import math
from collections import deque

# 다음 풀 문제: 실버 3

# 1449번 수리공 항승

# 첫째 줄에 물이 새는 곳의 개수 N과 테이프의 길이 L이 주어진다.
# N과 L은 1,000보다 작거나 같은 자연수
n, l = map(int, input().split())

# 둘째 줄에는 물이 새는 곳의 위치가 주어진다.
# 물이 새는 곳의 위치는 1,000보다 작거나 같은 자연수
spots = list(map(int, input().split()))

spots.sort()

start = spots[0]
cnt = 1

for spot in spots[1:]:
    if spot in range(start, start + l):
        continue
    else:
        start = spot
        cnt += 1

print(cnt)
