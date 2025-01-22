from sys import stdin as stdin

H, I, A, R, C = map(int, stdin.readline().split())
result = (H * I) - (A * R * C)
print(result)