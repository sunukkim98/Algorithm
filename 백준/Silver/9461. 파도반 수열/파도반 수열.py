import sys

def get_P(n):
    if n == 1:
        return 1
    if n == 2:
        return get_P(1)
    if n == 3:
        return get_P(2)
    if n == 4:
        return get_P(3) + get_P(1)
    if n == 5:
        return get_P(4)
    if n == 6:
        return get_P(1) + get_P(5)
    return get_P(n-1) + get_P(n-5)

def get_P_Dynamic(n):
    dp = [0] * (101)
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    dp[4] = 2
    dp[5] = 2
    dp[6] = 3
    for i in range(7, n+1):
        dp[i] = dp[i-1] + dp[i-5]
    return dp[n]

# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
T = int(sys.stdin.readline().strip())

# 각 테스트 케이스는 한 줄로 이루어져 있고, N이 주어진다.(1 <= N <= 100)
for _ in range(T):
    N = int(sys.stdin.readline().strip())

    # 출력: 각 테스트 케이스마다 P(N)을 출력한다.
    print(get_P_Dynamic(N))