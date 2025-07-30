import sys
input = sys.stdin.readline

n = int(input().strip())
m = list(map(int, input().split()))
for level in m:
    if level == 300:
        print(1, end=" ")
    elif level >= 275:
        print(2, end=" ")
    elif level >= 250:
        print(3, end=" ")
    else:
        print(4, end=" ")
