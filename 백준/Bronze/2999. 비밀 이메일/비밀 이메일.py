import sys
input = sys.stdin.readline

message = input().strip()
len = len(message)

C, R = 0, 0

for r in range(1, int(len / 2) + 1):
    for c in range(r, len + 1):
        if r * c == len:
            C, R = r, c

for i in range(C):
    for j in range(R):
        print(message[i+j*C], end='')
