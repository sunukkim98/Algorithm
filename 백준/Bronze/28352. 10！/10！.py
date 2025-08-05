import sys
input = sys.stdin.readline

n = int(input().strip())
dp = [0 for _ in range(n+1)]
dp[1] = 1
dp[2] = 1 * 2
for i in range(3, n+1):
    dp[i] = dp[i-1] * i
sec = dp[n]
print(sec // (7 * 24 * 60 * 60))
