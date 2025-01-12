import sys

# 금고의 위치를 나타내는 좌표를 입력받는다. (0 < x,y <= 1000000)
x, y = map(int, sys.stdin.readline().split())

# y가 0인 경우:
#     result = (1 + 6 * 1) + (6 * 2) + (6 * 3) + ... + (6 * x)
if y == 0:
    result = 1
    for i in range(x):
        result += 6 * (i + 1)
    print(result)
# x가 0인 경우:
#     result = (1 + 1 = 2) + ((6 * 1) + 1) + ((6 * 2) + 1) ... + (6 * (y - 1) + 1)
elif x == 0:
    result = 1
    for i in range(y):
        if i == 0:
            result += 1
        else:
            result += (6 * i) + 1
    print(result)
# 둘 다 0이 아닌 경우:
#     result = (1 + 6 * 1) + (6 * 2) + (6 * 3) + ... + (6 * x) + y
else:
    result = 1
    for i in range((x + y) - 1):
        result += 6 * (i + 1)
    result += y
    print(result)
