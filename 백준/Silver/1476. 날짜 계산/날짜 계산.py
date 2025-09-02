import sys
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline
import math

# 다음 풀 문제: 실버 5

# def lcm(x, y):
#     return x * y // math.gcd(x, y)
#
# def solution(arr):
#     while True:
#         arr.append(lcm(arr.pop(), arr.pop()))
#         if len(arr) == 1:
#             return arr[0]

e, s, m = map(int, input().split())

num = 1
while True:
    # if e == 15 and s == 28 and m == 19:
    #     num = solution([15, 28, 19])
    #     break
    # if num % 15 == e and num % 28 == s and num % 19 == m:
    #     break
    # else:
    #     num += 1
    if (num - e) % 15 == 0 and (num - s) % 28 == 0 and (num - m) % 19 == 0:
        break
    num += 1

print(num)
