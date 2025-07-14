import sys
input = sys.stdin.readline

k, n, m = map(int, input().split())
total_cost = k * n
if total_cost > m:
    print(total_cost - m)
else:
    print(0)
