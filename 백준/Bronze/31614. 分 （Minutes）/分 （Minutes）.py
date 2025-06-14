import sys
input = sys.stdin.readline

h = int(input().strip())
m = int(input().strip())
m += h * 60
print(m)
