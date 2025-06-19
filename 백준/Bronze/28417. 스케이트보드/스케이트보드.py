import sys
input = sys.stdin.readline

n = int(input().strip())
final_scores = []
for i in range(n):
    scores = list(map(int, input().split()))
    run_scores = scores[:2]
    trick_scores = scores[2:]
    trick_scores.sort()
    final_scores.append(max(run_scores) + trick_scores[-1] + trick_scores[-2])
print(max(final_scores))
