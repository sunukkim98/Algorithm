import sys
input = sys.stdin.readline

distance = int(input().strip())
if distance % 5 == 0:
    print(distance // 5)
else:
    print((distance // 5) + 1)
