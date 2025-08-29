import sys
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline
# import math

# 다음 풀 문제: 실버 3

n = int(input().strip())
cows = {}
cnt = 0
for _ in range(n):
    c_num, pos = map(int, input().split())
    if c_num not in cows:
        cows[c_num] = pos
    else:
        if cows[c_num] != pos:
            cows[c_num] = pos
            cnt += 1

print(cnt)
