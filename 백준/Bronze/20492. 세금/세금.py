import sys
input = sys.stdin.readline

N = int(input().strip())
tax = round(N * 0.22)
print(N - tax)
tax = round((N * 0.2) * 0.22)
print(N - tax)