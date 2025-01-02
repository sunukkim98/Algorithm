# 줄을 서 있는 사람의 수 N을 입력받는다.
# N번 반복:
#     Pi를 입력받는다. (1 <= Pi <= 1000)
# 입력받은 Pi를 오름차순으로 정렬한다.
# 정렬된 순서로 첫 번째 부터 뒤 순서까지 반복한다:
#     각 순번 전 순서까지 모두 더해 해당 순번의 순서에 더한다.
# 모두 더해진 순서를 합산한다.

import sys

n = int(input())

P = sys.stdin.readline().strip().split()

P_list = []
for pi in P:
    P_list.append(int(pi))

P_list.sort()

tmp = 0
sum = 0
for p in P_list:
    tmp += p
    p = tmp
    sum += p
print(sum)