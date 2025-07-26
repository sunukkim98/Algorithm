import sys
input = sys.stdin.readline

n, m = map(int, input().split())
if m <= n:
    if m < 3:
        print("NEWBIE!")
    else:
        print("OLDBIE!")
else:
    print("TLE!")
