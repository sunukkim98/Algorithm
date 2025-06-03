import sys
input = sys.stdin.readline

N, M = map(int, input().split())
N = (N // 2)
M = (M // 2)
print(min(N, M))
