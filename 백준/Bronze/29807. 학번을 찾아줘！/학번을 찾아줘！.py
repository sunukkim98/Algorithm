import sys
input = sys.stdin.readline

t = int(input().strip())
scores = list(map(int, input().split()))

if t < 5:
    scores += [0] * (5-t)

if scores[0] > scores[2]:
    num_1 = (scores[0] - scores[2]) * 508
else:
    num_1 = (scores[2] - scores[0]) * 108

if scores[1] > scores[3]:
    num_2 = (scores[1] - scores[3]) * 212
else:
    num_2 = (scores[3] - scores[1]) * 305

if t == 5:
    num_3 = scores[4] * 707
    total = num_1 + num_2 + num_3
else:
    total = num_1 + num_2

total *= 4763
print(total)
