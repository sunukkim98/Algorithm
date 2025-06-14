import sys
input = sys.stdin.readline

x = int(input().strip())
if x % 7 == 2:
    print(1)
else:
    print(0)
