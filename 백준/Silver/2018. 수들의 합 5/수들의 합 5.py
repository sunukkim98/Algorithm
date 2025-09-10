import sys
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline
# import math

# 다음 풀 문제: 실버 5

# 2018번 수들의 합 5

# 첫 줄에 정수 N이 주어진다.
n = int(input().strip())
end = 0
sum = 0
cnt = 0

for i in range(0, n):
    while sum < n and end < n:
        sum += end + 1
        end += 1
    if sum == n:
        cnt += 1
    sum -= i + 1

print(cnt)
