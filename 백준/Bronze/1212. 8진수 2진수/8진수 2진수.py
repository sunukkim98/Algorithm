import sys
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline
# import math

# 다음 풀 문제: 브론즈 2

oct = input().strip()
dec = int(oct, 8)
binary = bin(dec)
print(binary[2:])
