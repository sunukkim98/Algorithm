import sys
input = sys.stdin.readline

n = int(input().strip())
for i in range(n):
    input_num = int(input().strip())
    if input_num % 2 == 0:
        print(input_num, "is even")
    else:
        print(input_num, "is odd")