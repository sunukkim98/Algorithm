import sys
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline
# import math
from collections import deque

# 다음 풀 문제: 실버 4

# 2578번 빙고

# 첫째 줄부터 다섯째 줄까지 빙고판에 쓰여진 수가 가장 위 가로줄부터 차례대로 한 줄에 다섯 개씩 빈 칸을 사이에 두고 주어진다.
board = []
for _ in range(5):
    board.append(list(map(int, input().split())))

# print(board)

# 여섯째 줄부터 열째 줄까지 사회자가 부르는 수가 차례대로 한 줄에 다섯 개씩 빈 칸을 사이에 두고 주어진다.
# 빙고판에 쓰여진 수와 사회자가 부르는 수는 각각 1부터 25까지의 수가 한 번씩 사용된다.
numbers = []
for _ in range(5):
    numbers.append(list(map(int, input().split())))

check = [[0 for _ in range(5)] for _ in range(5)]
# print(check)

cnt = 0
bingo_cnt = 0
for i in range(5):
    for j in range(5):
        num = numbers[i][j]
        for k in range(5):
            for l in range(5):
                if board[k][l] == num:
                    check[k][l] = 1
        # print(check)
        cnt += 1
        if cnt > 10:
            for k in range(5):
                if check[k][0] and check[k][1] and check[k][2] and check[k][3] and check[k][4]:
                    # print("found bingo!")
                    bingo_cnt += 1
                if check[0][k] and check[1][k] and check[2][k] and check[3][k] and check[4][k]:
                    # print("found bingo!")
                    bingo_cnt += 1
            if check[0][0] and check[1][1] and check[2][2] and check[3][3] and check[4][4]:
                # print("found bingo!")
                bingo_cnt += 1
            if check[0][4] and check[1][3] and check[2][2] and check[3][1] and check[4][0]:
                # print("found bingo!")
                bingo_cnt += 1
            # print(bingo_cnt)
            if bingo_cnt > 2:
                print(cnt)
                exit()
            bingo_cnt = 0
