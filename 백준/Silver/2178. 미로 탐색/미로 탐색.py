import sys
input = sys.stdin.readline

from collections import deque

'''
문제:
    N * M크기의 배열로 표현되는 미로가 있다.
    101111
    101010
    101011
    111011
    미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 
    이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오.
    한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.
    칸을 셀 때에는 시작 위치와 도착 위치도 포함된다.
'''
def BFS(x, y, graph, N: int, M: int):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 범위 벗어난다면
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            # 0이라면
            if graph[nx][ny] == 0:
                continue
            # 1이라면 이동 가능
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[N-1][M-1]

'''
입력:
    첫째 줄에 두 정수 N, M (2 <= N, M <= 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다.
    각각의 수들은 붙어서 입력으로 주어진다.
'''
N, M = map(int, input().strip().split())
maze = []
for _ in range(N):
    maze.append(list(map(int, input().strip())))

'''
출력:
    첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.
'''
print(BFS(0, 0, graph=maze, N=N, M=M))