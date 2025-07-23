import sys
input = sys.stdin.readline

a, p, c = map(int, input().split())
print(max(a + c, p))
