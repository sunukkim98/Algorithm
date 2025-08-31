import sys
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline
# import math

# 다음 풀 문제: 실버 5

board = input().strip()
board = board.replace("XXXX", "AAAA")
board = board.replace("XX", "BB")
if "X" in board:
    print(-1)
else:
    print(board)
