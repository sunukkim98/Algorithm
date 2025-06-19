import sys
input = sys.stdin.readline

t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    p1_score = 0
    p2_score = 0
    for j in range(n):
        choice_1, choice_2 = input().split()
        if choice_1 == 'R' and choice_2 == 'S':
            p1_score += 1
        if choice_1 == 'S' and choice_2 == 'P':
            p1_score += 1
        if choice_1 == 'P' and choice_2 == 'R':
            p1_score += 1
        if choice_1 == 'S' and choice_2 == 'R':
            p2_score += 1
        if choice_1 == 'P' and choice_2 == 'S':
            p2_score += 1
        if choice_1 == 'R' and choice_2 == 'P':
            p2_score += 1
    if p1_score > p2_score:
        print("Player 1")
    elif p1_score == p2_score:
        print("TIE")
    else:
        print("Player 2")
