import sys
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline
# import math
# from collections import deque

# 다음 풀 문제: 그래프이론 10000번 이상 풀린 문제

# 9372번 상근이의 여행

def dfs(node, cnt):
    check[node] = 1
    for n in graph[node]:
        if check[n] == 0:
            cnt = dfs(n, cnt + 1)
    return cnt

# 첫 번째 줄에는 테스트 케이스의 수 T(T ≤ 100)가 주어지고,
t = int(input().strip())

for _ in range(t):
    # 첫 번째 줄에는 국가의 수 N(2 ≤ N ≤ 1 000)과 비행기의 종류 M(1 ≤ M ≤ 10 000) 가 주어진다.
    n, m = map(int, input().split())
    graph = {}
    for _ in range(m):
        a, b = map(int, input().split())
        if a in graph.keys():
            graph[a].append(b)
        else:
            graph[a] = [b]
        if b in graph.keys():
            graph[b].append(a)
        else:
            graph[b] = [a]
    check = [0]*(n + 1)
    cnt = dfs(1, 0)

    # 상근이가 모든 국가를 여행하기 위해 타야 하는 비행기 종류의 최소 개수를 출력한다
    print(cnt)
