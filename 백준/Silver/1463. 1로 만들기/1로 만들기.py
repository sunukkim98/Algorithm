import sys

def get_operation_times(n):
    if n == 1:
        return 0
    if n % 2 == 0:
        return min(get_operation_times(n - 1) + 1, get_operation_times(n / 2) + 1)
    if n % 3 == 0:
        return min(get_operation_times(n - 1) + 1, get_operation_times(n / 3) + 1)
    return get_operation_times(n - 1) + 1

def get_operation_time_Dynamic(n):
    dp = [0] * ((10 ** 6) + 1)
    for i in range(2, n+1):
        dp[i] = dp[i-1] + 1
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i//2] + 1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i//3] + 1)
    return dp[n]

N = int(sys.stdin.readline().strip())
# print(get_operation_times(N))
print(get_operation_time_Dynamic(N))