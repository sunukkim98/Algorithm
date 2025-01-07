# 금고의 위치를 나타내는 좌표를 입력받는다. (0 < x,y <= 1000000)
# x가 0인 경우:
#     좌표값 y=1초과부터 6*y가 증가한다.
# y가 0인 경우:
#     00 -> 10 -> 20 -> ... -> x0 값이 6*x만큼 증가
# 둘 다 0이 아닌 경우:
#     (x+y,0)에서 y좌표 값인 y만큼 값 증가

import sys

x, y = map(int, sys.stdin.readline().split())

if y == 0:
    result = 1
    for i in range(x):
        result += 6 * (i + 1)
    print(result)
elif x == 0:
    result = 1
    for i in range(y):
        if i == 0:
            result += 1
        else:
            result += (6 * i) + 1
    print(result)
else:
    result = 1
    for i in range((x + y) - 1):
        result += 6 * (i + 1)
    result += y
    print(result)
