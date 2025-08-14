import sys
input = sys.stdin.readline

# 다음 풀 문제: 브론즈 2

color = [
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0]
]

board = []
for _ in range(8):
    board.append(input().strip())

cnt = 0
for i in range(8):
    for j in range(8):
        if board[i][j] == 'F' and color[i][j] == 0:
            cnt += 1
print(cnt)
