import sys
input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))
X, Y = map(int, input().split())

cnt = 0
for score in A:
    if score >= Y:
        cnt += 1

# Output
print(int(N * X // 100), cnt)