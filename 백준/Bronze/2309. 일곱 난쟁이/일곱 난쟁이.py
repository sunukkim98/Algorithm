import sys
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline
# import math

# 다음 풀 문제: 브론즈 1

heights = []

for _ in range(9):
    height = int(input().strip())
    heights.append(height)

heights.sort()
sum = sum(heights)

for i in range(9):
    for j in range(i + 1, 9):
        if sum - heights[i] - heights[j] == 100:
            for k in range(9):
                if k == i or k == j:
                    pass
                else:
                    print(heights[k])
            exit()
