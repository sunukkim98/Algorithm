import sys
input = sys.stdin.readline

T = int(input().strip())
for i in range(T):
    scores = list(map(int, input().split()))
    scores.sort()
    valid_scores = scores[1:-1]
    if valid_scores[-1] - valid_scores[0] >= 4:
        print("KIN")
    else:
        print(sum(valid_scores))
