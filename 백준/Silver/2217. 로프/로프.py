import sys
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline
# import math

# 다음 풀 문제: 실버 4

# 2217번 로프

# 첫째 줄에 정수 N이 주어진다.
n = int(input().strip())

# 다음 N개의 줄에는 각 로프가 버틸 수 있는 최대 중량이 주어진다. 이 값은 10,000을 넘지 않는 자연수이다.
weights = []
for _ in range(n):
    weights.append(int(input().strip()))

# weights.sort(reverse=True)
#
# res = 0
# for i in range(1, n + 1):
#     # print(weights[:i])
#     candidate_1 = weights[:i][-1] * i
#     candidate_2 = weights[0]
#     if res < max(candidate_1, candidate_2):
#         res = max(candidate_1, candidate_2)
#
# print(res)

weights.sort()
ans = []
for weight in weights:
    ans.append(weight * n)
    n -= 1
print(max(ans))
