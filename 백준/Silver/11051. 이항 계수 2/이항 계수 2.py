import sys
input = sys.stdin.readline

'''
문제:
    자연수 N과 정수 K가 주어졌을 때 이항 계수 (N K)를 10,007로 나눈 나머지를 구하는 프로그램을 작성하시오.
'''

'''
입력:
    첫째 줄에 N과 K가 주어진다. (1 <= N <= 1,000, 0 <= K <= N)
'''
N, K = map(int, input().strip().split())

# 조건에 맞는 이항계수 공식:
#     N! / (K!(N-K)!)
dp = [1] * 1001
dp[2] = 2
for i in range(3, N + 1):
    dp[i] = dp[i-1] * i
N_f = dp[N]
K_f = dp[K]
NmK_f = dp[N-K]
result = (N_f // (K_f * NmK_f)) % 10007

'''
출력:
    (N K)를 10,007로 나눈 나머지를 출력한다.
'''
print(int(result))