import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
print(int(a * max(b, c) / min(b, c)))
