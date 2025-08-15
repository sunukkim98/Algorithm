import sys
input = sys.stdin.readline

# 다음 풀 문제: 실버 5

N = int(input())
ans = 0
for i in range(7):
    if N & (1 << i):
        ans += 1
print(ans)
