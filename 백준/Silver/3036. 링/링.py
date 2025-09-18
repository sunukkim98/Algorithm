import sys
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline
# import math
# from collections import deque

# 다음 풀 문제: 실버 4

# 3036번 링

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

# 첫째 줄에 링의 개수 N이 주어진다. (3 ≤ N ≤ 100)
n = int(input().strip())

# 다음 줄에는 링의 반지름이 상근이가 바닥에 놓은 순서대로 주어진다. 반지름은 1과 1000를 포함하는 사이의 자연수이다.
radius_list = list(map(int, input().split()))

for i in range(1, n):
    a = radius_list[0]
    b = radius_list[i]
    gcd_num = gcd(a, b)
    a //= gcd_num
    b //= gcd_num

    print(f"{a}/{b}")
