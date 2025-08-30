import sys
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline
# import math

# 다음 풀 문제: 실버 4

# 1940번 주몽

# 첫째 줄에는 재료의 개수 N(1 ≤ N ≤ 15,000)이 주어진다.
n = int(input().strip())

# 두 번째 줄에는 갑옷을 만드는데 필요한 수 M(1 ≤ M ≤ 10,000,000) 주어진다.
m = int(input().strip())

# 마지막으로 셋째 줄에는 N개의 재료들이 가진 고유한 번호들이 공백을 사이에 두고 주어진다.
prices = list(map(int, input().split()))

prices.sort()
cnt = 0
# # if n % 2 == 0:
# #     mid = n // 2
# # else:
# #     mid = n // 2 + 1
# for i in range(n):
#     for j in range(i + 1, n):
#         # print(prices[i], prices[j])
#         if prices[i] + prices[j] > m:
#             break
#         if prices[i] + prices[j] == m:
#             # print(prices[i], prices[j])
#             cnt += 1

left, right = 0, n - 1

while left < right:
    if prices[left] + prices[right] < m:
        left += 1
    elif prices[left] + prices[right] > m:
        right -= 1
    else:
        cnt += 1
        left += 1
        right -= 1

print(cnt)
