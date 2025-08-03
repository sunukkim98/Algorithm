import sys
input = sys.stdin.readline

n = int(input().strip())
d_point, p_point = 0, 0
for _ in range(n):
    predict = input().strip()
    if predict == 'D':
        d_point += 1
    else:
        p_point += 1
    if abs(d_point - p_point) >= 2:
        break
print(f"{d_point}:{p_point}")
