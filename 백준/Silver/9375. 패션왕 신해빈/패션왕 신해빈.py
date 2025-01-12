# 첫째 줄에 테스트 케이스가 주어진다.(최대 100)
# 테스트 케이스만큼 반복:
#     각 테스트 케이스의 첫째 줄에는 해빈이가 가진 의상의 수 n(0 <= n <= 30)이 주어진다.
#     다음 n개에는:
#         해빈이가 가진 의상의 이름과 의상의 종류가 공백으로 구분되어 주어진다. 같은 종류의 의상은 하나만 입을 수 있다.
#         (모든 문자열은 1이상 20이하의 알파벳 소문자로 이루어져있으며 같은 이름을 가진 의상은 존재하지 않음)
#         출력: 각 테스트 케이스에 대해 해빈이가 알몸이 아닌 상태로 의상을 입을 수 있는 경우의 수

import sys
from collections import defaultdict

test_case = int(sys.stdin.readline().strip())
for i in range(test_case):
    num_of_cloths = int(sys.stdin.readline().strip())
    cloths = defaultdict(list)
    for j in range(num_of_cloths):
        line = sys.stdin.readline().strip().split()
        val = line[0]
        key = line[1]
        cloths[key].append(val)
    # print(cloths)
    # print(len(cloths))
    cnt = 1
    for j in cloths:
        cnt *= (len(cloths[j]) + 1)
    print(cnt - 1)