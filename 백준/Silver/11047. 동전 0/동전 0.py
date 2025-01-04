# 동전의 종류의 개수인 N과 만들 가치의 합 K를 입력받는다. (1 <= N <= 10, 1 <= K <= 100,000,000)
# N개의 줄에 걸쳐 동전 종류의 가치 A_i를 입력받는다. (1 <= A_i <= 1,000,000, A_1 = 1, i>= 2인 경우 A_i는 A_i = A_(i-1)의 배수)
# K원을 만드는데 필요한 동전 개수의 최솟값을 출력한다.
# 최솟값을 구하는 방법
# A_i의 순서 역순으로 K와 비교해 K보다 작거나 같다면 빼고 그 결과가 0이 된다면 뺀 값들의 개수를 모두 더해 출력한다.

import sys

N, K = map(int, sys.stdin.readline().strip().split())
A = []

for i in range(N):
    A_i = int(sys.stdin.readline().strip())
    A.append(A_i)
# A.sort(reverse=True)
A.reverse()

cnt = 0
i = 0
while K != 0:
    if A[i] <= K:
        cnt += K // A[i]
        K %= A[i]

    else:
        i += 1
print(cnt)