import sys
input = sys.stdin.readline

# 다음 풀 문제: 실버 3

# 1004번 어린왕자

# 입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다.
t = int(input().strip())
# 그 다음 줄부터 각각의 테스트케이스에 대해 첫째 줄에 출발점 (x1, y1)과 도착점 (x2, y2)이 주어진다.
for _ in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input().strip())

    cnt = 0

    for _ in range(n):
        c_x, c_y, r = map(int, input().split())
        dist1 = (x1 - c_x) ** 2 + (y1 - c_y) ** 2
        dist2 = (x2 - c_x) ** 2 + (y2 - c_y) ** 2
        if (dist1 < r ** 2 and dist2 > r ** 2) or (dist1 > r ** 2 and dist2 < r ** 2):
            cnt += 1
            # print(c_x, c_y, r)

    print(cnt)

