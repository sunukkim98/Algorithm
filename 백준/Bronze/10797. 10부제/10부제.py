import sys
input = sys.stdin.readline

day = int(input().strip())
car_num = list(map(int, input().split()))
cnt = 0
for num in car_num:
    if num == day:
        cnt += 1
print(cnt)