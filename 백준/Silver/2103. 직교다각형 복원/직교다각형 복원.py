# 점의 개수 N을 입력받는다.
# 다음 N개의 줄에는:
#     x,y(0 <= x, y <= 10,000)좌표가 주어진다.

import sys
from collections import defaultdict

n = int(sys.stdin.readline().strip())
vX = defaultdict(list)
vY = defaultdict(list)
for i in range(n):
    x, y = map(int, sys.stdin.readline().strip().split())
    vX[x].append(y)
    vY[y].append(x)
total = 0
for i in range(10001):
    vX[i].sort()
    vY[i].sort()
    for j in range(0, len(vX[i]), 2):
        total += vX[i][j + 1] - vX[i][j]
    for j in range(0, len(vY[i]), 2):
        total += vY[i][j + 1] - vY[i][j]

print(total)