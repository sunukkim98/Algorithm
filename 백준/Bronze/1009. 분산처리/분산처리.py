import sys
input = sys.stdin.readline

patterns = [
    [1],
    [2, 4, 8, 6],
    [3, 9, 7, 1],
    [4, 6],
    [5],
    [6],
    [7, 9, 3, 1],
    [8, 4, 2, 6],
    [9, 1],
    [0]
]

t = int(input().strip())
for _ in range(t):
    a, b = map(int, input().split())
    if a % 10 == 1:
        print(1)
    elif a % 10 == 2:
        print(patterns[1][(b % 4) - 1])
    elif a % 10 == 3:
        print(patterns[2][b % 4 - 1])
    elif a % 10 == 4:
        print(patterns[3][b % 2 - 1])
    elif a % 10 == 5:
        print(5)
    elif a % 10 == 6:
        print(6)
    elif a % 10 == 7:
        print(patterns[6][b % 4 - 1])
    elif a % 10 == 8:
        print(patterns[7][b % 4 - 1])
    elif a % 10 == 9:
        print(patterns[8][b % 2 - 1])
    elif a % 10 == 0:
        print(10)
