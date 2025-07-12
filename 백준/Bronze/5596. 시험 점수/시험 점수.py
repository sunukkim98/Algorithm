import sys
input = sys.stdin.readline

total_score = []
for _ in range(2):
    info, math, sci, eng = map(int, input().split())
    total_score.append(info + math + sci + eng)
print(max(total_score))
