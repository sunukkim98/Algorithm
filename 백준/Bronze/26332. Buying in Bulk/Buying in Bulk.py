import sys
input = sys.stdin.readline

n = int(input().strip())
for _ in range(n):
    c, p = map(int, input().split())
    print(c, p)
    if c == 1:
        total_p = p
        print(p)
    else:
        total_p = c * p
        discount = 2 * (c - 1)
        total_p -= discount
        print(total_p)
