import sys
input = sys.stdin.readline

A, B, C = map(int, input().strip().split())
times = [0] * 101
for _ in range(3):
    start, end = map(int, input().strip().split())
    for i in range(start, end):
        times[i] += 1
car_time = 0
for i in range(101):
    if times[i] == 1:
        car_time += A
    elif times[i] == 2:
        car_time += B * 2
    elif times[i] == 3:
        car_time += C * 3

print(car_time)