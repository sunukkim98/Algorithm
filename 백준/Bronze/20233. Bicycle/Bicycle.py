import sys
input = sys.stdin.readline

a = int(input().strip())
x = int(input().strip())
b = int(input().strip())
y = int(input().strip())

T = int(input().strip())

rest_time_1 = T - 30
if rest_time_1 < 0:
    rest_time_1 = 0
rest_time_2 = T - 45
if rest_time_2 < 0:
    rest_time_2 = 0

option_1 = a + (rest_time_1 * x) * 21
option_2 = b + (rest_time_2 * y) * 21

print(option_1, option_2)