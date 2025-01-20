from sys import stdin as stdin

def get_num_of_ways(n):
    dp = [0] * (1002)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]


# 첫째 줄에 n이 주어진다 (1 <= n <= 1,000)
n = int(stdin.readline().strip())

# 출력: 2xn 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다
result = get_num_of_ways(n) % 10007
print(result)