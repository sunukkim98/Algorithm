from sys import stdin as stdin

def get_fibonacci(n):
    dp = [0] * (47)
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

n = int(stdin.readline().strip())
print(get_fibonacci(n))