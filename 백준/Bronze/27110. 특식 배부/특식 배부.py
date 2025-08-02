import sys
input = sys.stdin.readline

n = int(input().strip())
a, b, c = map(int, input().split())
sum = min(n, a) + min(n, b) + min(n, c)
print(sum)
