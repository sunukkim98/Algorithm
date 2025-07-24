import sys
input = sys.stdin.readline

n = int(input().strip())
flag = True
for i in range(3):
    digits = list(map(int, input().split()))
    if 7 not in digits:
        flag = False
if flag:
    print(777)
else:
    print(0)
