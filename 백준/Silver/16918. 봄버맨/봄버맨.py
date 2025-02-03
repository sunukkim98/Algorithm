import sys
input = sys.stdin.readline

from collections import deque

def print_graph(graph):
    for row in graph:
        # 요소들을 리스트 형태가 아닌 풀어서 출력
        print(*row, sep='')

def install_bomb(R, C, graph):
    for i in range(R):
        for j in range(C):
            if graph[i][j] == '.':
                graph[i][j] = 'O'
    return graph

def find_bomb(R, C, graph, dq):
    for i in range(R):
        for j in range(C):
            if graph[i][j] == 'O':
                dq.append([i, j])
    return dq

def bombing(dq, graph):
    while dq:
        y, x = dq.popleft()
        graph[y][x] = '.'
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if (0 <= ny < R) and (0 <= nx < C):
                graph[ny][nx] = '.'
    return graph

# 첫째 줄에 R, C, N (1 <= R, C, N <= 200)이 주어진다.
R, C, N = map(int, input().split())

graph = [list(input().strip()) for _ in range(R)]

# 방향정의: 상하좌우
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

if N % 2 != 0:
    N -= 1
    while N > 0:
        dq = deque()
        dq = find_bomb(R, C, graph, dq)
        graph = install_bomb(R, C, graph)
        N -= 1
        if N == 0:
            break
        graph = bombing(dq, graph)
        N -= 1
    print_graph(graph)
else:
    graph = [['O'] * C for _ in range(R)]
    print_graph(graph)