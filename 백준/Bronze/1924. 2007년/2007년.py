import sys
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline
import math

# 다음 풀 문제: 브론즈 1

# 1924번 2007년

# 첫째 줄에 빈 칸을 사이에 두고 x(1 ≤ x ≤ 12)와 y(1 ≤ y ≤ 31)이 주어진다.
x, y = map(int, input().split())

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

day_of_the_week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

if x > 1:
    for i in range(x-1):
        y += days[i]

# print(y)
print(day_of_the_week[y % 7])
