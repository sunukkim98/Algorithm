import sys
input = sys.stdin.readline

n = int(input().strip())
pirates = [i for i in range(1, n + 1)]
cnt = 0
while len(pirates) != 0:
    print(pirates.pop(0), end=' ')
    cnt += 1
    if cnt == 6 or len(pirates) == 0:
        cnt = 0
        print("Go!", end=' ')
