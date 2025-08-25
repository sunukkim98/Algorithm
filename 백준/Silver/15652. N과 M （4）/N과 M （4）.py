import sys
input = sys.stdin.readline

# 다음 풀 문제: 실버 3

def dfs(cnt, m, n, s):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(cnt, n+1):
        s.append(i)
        dfs(i, m, n, s)
        s.pop()

n, m = map(int, input().split())

s = []

dfs(1, m, n, s)
