import sys
input = sys.stdin.readline

n, m = map(int, input().split())
if n % 3 == 0 or m % 3 == 0:
    print("YES")
else:
    print("NO")
