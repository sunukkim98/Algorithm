import sys
input = sys.stdin.readline

# 다음 풀 문제: 실버 5

s = input().strip()

cnt = 0
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        cnt += 1
print((cnt + 1) // 2)
