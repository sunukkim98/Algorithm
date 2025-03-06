import sys
input = sys.stdin.readline

'''
문제: 2156 포도주 시식
    1. 포도주 잔을 선택하면 그 잔에 들어있는 포도주는 모두 마셔야 하고, 마신 후에는 원래 위치에 다시 놓아야 한다.
    2. 연속으로 놓여 있는 3잔을 모두 마실 수는 없다.
    1부터 n까지의 번호가 붙어 있는 n개의 포도주 잔이 순서대로 테이블 위에 놓여 있고, 각 포도주 잔에 들어있는 포도주의 양이 주어졌을 때, 효주
    를 도와 가장 많은 양의 포도주를 마실 수 있도록 하는 프로그램을 작성하시오.
'''

'''
입력:
    첫째 줄에 포도주 잔의 개수 n이 주어진다. (1 <= n <= 10,000) 둘째 줄부터 n+1번째 줄까지 포도주 잔에 들어있는 포도주의 양이 순서대로
    주어진다. 포도주의 양은 1,000 이하의 음이 아닌 정수이다.
'''
n = int(input())
num_of_wine = [int(input()) for _ in range(n)]

dp = [0] * n
dp[0] = num_of_wine[0]
if n > 1:
    dp[1] = num_of_wine[0] + num_of_wine[1]
if n > 2:
    dp[2] = max(num_of_wine[2] + num_of_wine[1], num_of_wine[2] + num_of_wine[0], dp[1])

for i in range(3, n):
    dp[i] = max(dp[i-1], dp[i-3]+num_of_wine[i-1]+num_of_wine[i], dp[i-2]+num_of_wine[i])

'''
출력:
    첫째 줄에 최대로 마실 수 있는 포도주의 양을 출력한다.
'''
print(dp[n-1])