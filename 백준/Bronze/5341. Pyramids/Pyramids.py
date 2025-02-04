import sys
input = sys.stdin.readline

while True:
    size = int(input())
    if size == 0:
        break
    temp = 0
    for i in range(1, size + 1):
        temp += i
    print(temp)