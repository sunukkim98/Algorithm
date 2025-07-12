import sys
input = sys.stdin.readline

sec = 0
for _ in range(4):
    sec += int(input().strip())
min = sec // 60
sec = sec % 60
print(min)
print(sec)
