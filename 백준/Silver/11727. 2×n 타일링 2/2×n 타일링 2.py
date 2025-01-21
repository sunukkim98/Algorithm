from sys import stdin as stdin

def get_num_of_ways(n):
    dp = [0] * (1002)
    dp[1] = 1
    dp[2] = 3
    for i in range(3, n+1):
        dp[i] = dp[i-1] + (2 * dp[i-2])
    return dp[n]

n = int(stdin.readline().strip())

print(get_num_of_ways(n) % 10007)