import sys
input = sys.stdin.readline

n, k = map(int, input().split())
scores = list(map(int, input().split()))
levels = []
for score in scores:
    # print((score * 100) // n)
    p = (score * 100) // n
    if p >= 0 and p <= 4:
        levels.append(1)
    elif p > 4 and p <= 11:
        levels.append(2)
    elif p > 11 and p <= 23:
        levels.append(3)
    elif p > 23 and p <= 40:
        levels.append(4)
    elif p > 40 and p <= 60:
        levels.append(5)
    elif p > 60 and p <= 77:
        levels.append(6)
    elif p > 77 and p <= 89:
        levels.append(7)
    elif p > 89 and p <= 96:
        levels.append(8)
    elif p > 96 and p <= 100:
        levels.append(9)

for level in levels:
    print(level, end=" ")
