import sys
input = sys.stdin.readline

s, t, d = map(int, input().split())
res = (d // (s * 2)) * t
print(res)
