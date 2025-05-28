import sys
input = sys.stdin.readline

solved_prob = [12, 11, 11, 10, 9, 9, 9, 8, 7, 6, 6]
score = [1600, 894, 1327, 1311, 1004, 1178, 1357, 837, 1055, 556, 773]

N = int(input().strip())
print(solved_prob[N-1], score[N-1])