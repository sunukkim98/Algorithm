import sys
input = sys.stdin.readline

n, x = map(int, input().split())
a = list(map(int, input().split()))
costs = []
for i in range(n-1):
    costs.append(a[i] * x + a[i+1] * x)
print(min(costs))
