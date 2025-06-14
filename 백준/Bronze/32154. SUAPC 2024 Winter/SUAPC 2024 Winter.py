import sys
input = sys.stdin.readline

score_board = [
    ['A','B','C','D','E','F','G','H','J','L','M'],
    ['A','C','E','F','G','H','I','L','M'],
    ['A','C','E','F','G','H','I','L','M'],
    ['A','B','C','E','F','G','H','L','M'],
    ['A','C','E','F','G','H','L','M'],
    ['A','C','E','F','G','H','L','M'],
    ['A','C','E','F','G','H','L','M'],
    ['A','C','E','F','G','H','L','M'],
    ['A','C','E','F','G','H','L','M'],
    ['A','B','C','F','G','H','L','M']
]
n = int(input().strip())
print(len(score_board[n-1]))
for i in range(len(score_board[n-1])):
    print(score_board[n-1][i], end=' ')
