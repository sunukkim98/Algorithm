import sys
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline
# import math
from collections import deque

def judge_prime(num: int):
    result = True
    for i in range(2, num):
        if num % i == 0:
            result = False
            break
    return result

# 다음 풀 문제: 실버 4

# 2960번 에라토스테네스의 체

# 첫째 줄에 N과 K가 주어진다. (1 ≤ K < N, max(1, K) < N ≤ 1000)
n, k = map(int, input().split())

# numbers라는 2부터 k까지 정수가 들어있는 리스트 생성
numbers = [i for i in range(2, n + 1)]
# print(numbers)

cnt = 0
while True:
    if len(numbers) == 0:
        break
    if judge_prime(numbers[0]):
        prime_num = numbers[0]
        # print(prime_num)
        for num in numbers:
            if num % prime_num == 0:
                numbers.remove(num)
                cnt += 1
                if cnt == k:
                    print(num)
                    exit()
    # print(numbers)
