import sys
# input = sys.stdin.readline

cnt = 0
while True:
    try:
        number = input()
        cnt += 1
    except EOFError:
        break
print(cnt)