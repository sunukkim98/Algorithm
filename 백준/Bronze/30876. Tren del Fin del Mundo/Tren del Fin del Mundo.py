import sys
input = sys.stdin.readline

# 다음 풀 문제: 브론즈 2

n = int(input().strip())
r_x, r_y = 9999, 9999
for _ in range(n):
    x, y = map(int, input().split())
    if y < r_y:
        r_x, r_y = x, y
print(r_x, r_y)
