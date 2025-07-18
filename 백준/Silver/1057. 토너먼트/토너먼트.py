import sys
input = sys.stdin.readline

n, jimin_num, hansoo_num = map(int, input().split())
round = 0
while jimin_num != hansoo_num:
    jimin_num -= jimin_num // 2
    hansoo_num -= hansoo_num // 2
    round += 1
print(round)
