import sys

# 입력:
# 첫째 줄에는 최백준 조교가 가진 돈 n과 돈을 받으러 온 생명체의 수 m이 주어진다.(1 <= m <= n <= 10^1000, m과 n은 10진수 정수)
n, m = map(int, sys.stdin.readline().strip().split())

# 출력:
# 첫째 줄에 생명체 하나에게 돌아가는 돈의 양을 출력
aver_n = n // m
print(aver_n)
# 그리고 두 번째 줄에는 1원씩 분배할 수 없는 남는 돈을 출력
remain_money = n % m
print(remain_money)