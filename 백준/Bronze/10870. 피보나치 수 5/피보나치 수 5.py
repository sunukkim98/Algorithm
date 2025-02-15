import sys
input = sys.stdin.readline

'''
문제:
    n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.
'''
def get_fibonacci(n: int):
    dp = [0] * 21
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

'''
입력:
    첫째 줄에 n이 주어진다. n은 20보다 작거나 같은 자연수 또는 0이다.
'''
n = int(input().strip())

'''
출력:
    첫째 줄에 n번째 피보나치 수를 출력한다.
'''
print(get_fibonacci(n))