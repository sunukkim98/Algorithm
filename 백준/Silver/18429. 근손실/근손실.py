import sys
input = sys.stdin.readline

from itertools import permutations as p

# 첫째 줄에 자연수 N과 K가 공백을 기준으로 구분되어 주어진다.
N, K = map(int, input().split())

# 둘째 줄에 각 운동 키트의 중량 증가량 A가 공백을 기준으로 구분되어 주어진다.
A = input().split()

# print(A)
A_p = p(A, N)
cnt = 0
for a in A_p:
    weight = 500
    for i in range(N):
        # print(a[i], end='')
        weight += int(a[i])
        weight -= K
        if weight < 500:
            break
        if i == N - 1:
            cnt += 1

print(cnt)