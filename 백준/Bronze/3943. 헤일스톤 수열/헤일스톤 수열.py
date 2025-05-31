import sys
input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    n = int(input().strip())
    max_num = n
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = (n * 3) + 1
        max_num = int(max(n, max_num))
    print(max_num)
