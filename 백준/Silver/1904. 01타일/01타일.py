import sys
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline
# import math
# from collections import deque

# 다음 풀 문제: 실버 3

# 1904번 01타일

# 첫 번째 줄에 자연수 N이 주어진다.
n = int(input().strip())

dp = [0] * 10000001
dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746

# 첫 번째 줄에 지원이가 만들 수 있는 길이가 N인 모든 2진 수열의 개수를 15746으로 나눈 나머지를 출력한다.
print(dp[n])

