import sys
input = sys.stdin.readline

w, h = map(int, input().strip().split())
res = (w + h) - ((w ** 2 + h ** 2) ** 0.5)
print(res)