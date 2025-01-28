import sys
input = sys.stdin.readline

def get_factorial(n: int):
    dp = [1] * 100
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] * i
    return dp[n]

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    result = get_factorial(M) // (get_factorial(N) * get_factorial(M - N))
    print(result)
