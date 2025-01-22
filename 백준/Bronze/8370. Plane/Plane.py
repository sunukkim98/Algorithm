from sys import stdin as stdin

n1, k1, n2, k2 = map(int, stdin.readline().split())
result = (n1 * k1) + (n2 * k2)
print(result)