import sys
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline
# import math

# 다음 풀 문제: 실버 5

# 1789번 수들의 합

# 첫째 줄에 자연수 S(1 ≤ S ≤ 4,294,967,295)가 주어진다.
s = int(input().strip())

sum = 0
n = 1
while True:
    if sum + n > s:
        print(n-1)
        break
    elif sum + n == s:
        print(n)
        break
    else:
        sum += n
        n += 1
