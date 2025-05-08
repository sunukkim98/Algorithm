import sys

input = sys.stdin.readline

T = int(input().strip())

for i in range(T):
    N = int(input().strip())
    line = input().split()
    for j in range(len(line)):
        line[j] = int(line[j])
    line.sort()
    print(line[0], line[-1])