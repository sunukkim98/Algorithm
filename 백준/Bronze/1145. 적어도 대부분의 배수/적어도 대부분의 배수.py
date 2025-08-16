import sys
input = sys.stdin.readline

# 다음 풀 문제: 브론즈 1

import math
from itertools import combinations

def solution(arr):
    def lcm(x, y):
        return x * y // math.gcd(x, y)

    while True:
        arr.append(lcm(arr.pop(), arr.pop()))
        if len(arr) == 1:
            return arr[0]

nums = list(map(int, input().split()))
# print(nums)

tmp = []
for i in combinations(nums, 3):
    tmp.append(solution(list(i)))
print(min(tmp))
