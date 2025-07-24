import sys
input = sys.stdin.readline

a, b = map(int, input().split())
m = (b - a) / 400
prob = 1 / (1 + (10 ** m))
print(prob)
