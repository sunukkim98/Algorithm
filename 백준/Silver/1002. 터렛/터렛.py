import sys
input = sys.stdin.readline

# input
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
T = int(input())

for _ in range(T):
    """
    각 테스트 케이스는 다음과 같이 이루어져 있다.
    한 줄에 공백으로 구분 된 여섯 정수 x1, y1, r1, x2, y2, r2가 주어진다.
    """
    x1, y1, r1, x2, y2, r2 = map(int, input().strip().split())

    # X1 = 조규현의 위치, X2 = 백승환의 위치, distance = X1과 X2 사이의 거리
    distance = (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** (1/2)

    if distance == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if (r1 + r2 == distance) or (abs(r1 - r2) == distance):
            print(1)
        elif (r1 + r2 > distance) and (abs(r1 - r2) < distance):
            print(2)
        else:
            print(0)