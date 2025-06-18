import sys
input = sys.stdin.readline

x = int(input().strip())
y = int(input().strip())
while x <= y:
    print(f"All positions change in year {x}")
    x += 60
