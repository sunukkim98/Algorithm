import sys
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline
# import math

# 다음 풀 문제: 실버 4

# 2003번 수들의 합 2

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
left, right = 0, 1
cnt = 0

while right <= n and left <= right:
    if sum(numbers[left:right]) == m:
        cnt += 1
        right += 1
    elif sum(numbers[left:right]) < m:
        right += 1
    else:
        left += 1

print(cnt)