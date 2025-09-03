import sys
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline
import math

# 다음 풀 문제: 브론즈 2

a, b = map(int, input().split())
c, d = map(int, input().split())
if a + c < b + d:
    print("Hanyang Univ.")
elif a + c > b + d:
    print("Yongdap")
else:
    print("Either")
