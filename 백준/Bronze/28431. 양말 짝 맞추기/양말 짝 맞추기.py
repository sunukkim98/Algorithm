import sys
input = sys.stdin.readline

num = []
socks = dict()
for i in range(0, 10):
    socks[i] = 0
for _ in range(5):
    # num.append(input().strip())
    socks[int(input().strip())] += 1
for i in range(0, 10):
    if socks[i] % 2 != 0 and socks[i] != 0:
        print(i)
