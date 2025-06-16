import sys
input = sys.stdin.readline

while True:
    cnt = 0
    line = input().split()
    if line[0] == '#' and line[1] == '0' and line[2] == '0':
        break
    if int(line[1]) > 17 or int(line[2]) >= 80:
        print(f"{line[0]} Senior")
    else:
        print(f"{line[0]} Junior")
