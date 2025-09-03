import sys
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline
import math

# 다음 풀 문제: 브론즈 1

# 1373번 2진수 8진수

# 첫째 줄에 2진수가 주어진다. 주어지는 수의 길이는 1,000,000을 넘지 않는다.
two_proceedings = input().strip()

d = int(two_proceedings, 2)

# 첫째 줄에 주어진 수를 8진수로 변환하여 출력한다.
print(oct(d)[2:])
