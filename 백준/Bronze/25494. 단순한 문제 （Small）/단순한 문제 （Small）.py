import sys
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    a, b, c = map(int, input().split())
    cnt = 0
    for i in range(1, a+1):
        for j in range(1, b+1):
            for k in range(1, c+1):
                if i % j == j % k and j % k == k % i:
                    # print(i, j, k)
                    cnt += 1
    print(cnt)
