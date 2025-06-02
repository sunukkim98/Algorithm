import sys
input = sys.stdin.readline

N = int(input().strip())
for _ in range(N):
    passwd = input().strip()
    if len(passwd) > 5 and len(passwd) < 10:
        print("yes")
    else:
        print("no")