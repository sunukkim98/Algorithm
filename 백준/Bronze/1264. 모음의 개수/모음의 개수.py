import sys
input = sys.stdin.readline

while True:
    cnt = 0
    line = input().strip()
    if line == '#':
        break
    line = line.lower()
    cnt += line.count('a')
    cnt += line.count('e')
    cnt += line.count('i')
    cnt += line.count('o')
    cnt += line.count('u')
    print(cnt)
