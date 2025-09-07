import sys
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline
# import math

# 다음 풀 문제: 브론즈 1

# 2851번 슈퍼 마리오

# 총 10개의 줄에 각각의 버섯의 점수가 주어진다. 이 값은 100보다 작거나 같은 양의 정수이다. 버섯이 나온 순서대로 점수가 주어진다.
scores = []
for _ in range(10):
    scores.append(int(input().strip()))

candidate_1 = 0
candidate_2 = 0

temp = []
for i in range(10):
    temp.append(scores[i])
    if sum(temp) >= 100:
        candidate_1 = sum(temp[:-1])
        candidate_2 = sum(temp)
        break
# print(candidate_1, candidate_2)

if candidate_1 == 0 and candidate_2 == 0:
    candidate_1 = sum(temp)
    candidate_2 = sum(temp)

if abs(100 - candidate_1) < abs(100 - candidate_2):
    print(candidate_1)
elif abs(100 - candidate_1) < abs(100 - candidate_2):
    print(max(candidate_1, candidate_2))
else:
    print(candidate_2)
