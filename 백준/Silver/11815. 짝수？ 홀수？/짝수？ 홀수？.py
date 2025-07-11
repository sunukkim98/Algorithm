import sys
input = sys.stdin.readline

# # 시간초과
# n = int(input().strip())
# X = list(map(int, input().split()))
# for i in range(n):
#     x = X[i]
#     cnt = 0
#     for j in range(1, x + 1):
#         if x % j == 0:
#             cnt += 1
#     if cnt % 2 == 0:
#         print(0, end=' ')
#     else:
#         print(1, end=' ')

# 제곱수로 표현되는 경우만 약수의 개수가 홀수

n = int(input().strip())
X = list(map(int, input().split()))

for x in X:
    if x == int(x ** (1/2)) ** 2:
        print(1, end=' ')
    else:
        print(0, end=' ')
