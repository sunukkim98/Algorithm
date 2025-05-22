import sys
input = sys.stdin.readline

while True:
    B, N = map(int, input().split())
    if B == 0 and N == 0:
        break
    A = 0
    while (abs((A ** N) - B)) > (abs(((A + 1) ** N) - B)):
        A += 1
    print(A)