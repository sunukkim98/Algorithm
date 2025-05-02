import sys
input = sys.stdin.readline

N, M = map(int, input().split())

area = N * M
print(area // 2)