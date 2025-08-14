import sys
input = sys.stdin.readline

# 다음 풀 문제: 브론즈 3

while True:
    n = input().strip()
    if n == '0':
        break
    blank = (len(n) - 1) + 2
    for num in n:
        if num == '1':
            blank += 2
        elif num == '0':
            blank += 4
        else:
            blank += 3
    print(blank)

