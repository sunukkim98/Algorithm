import sys
input = sys.stdin.readline

from collections import deque

def bfs():
    while dq: # dq가 빌 때까지 반복
        y, x = dq.popleft()
        for dy, dx in directions: # 현제 위치에서 4방향을 확인
            Y, X = y + dy, x + dx

            # 유효한 범위이고 방문하지 않은 칸이라면 큐에 추가후 해당 칸의 값 + 1로 업데이트
            if (0 <= Y < n) and (0 <= X < m) and graph[Y][X] == '0':
                dq.append((Y, X))
                graph[Y][X] = graph[y][x] + 1

# n, m이 공백으로 구분되어 주어진다.
n, m = map(int, input().split())

# 그래프 생성: n개의 줄에 걸쳐 입력
graph = [list(input().strip()) for _ in range(n)]

# 방향정의: 상하좌우
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 1인 위치 찾아 dq에 추가후 0으로 초기화
dq = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == '1':
            graph[i][j] = 0
            dq.append((i, j))

bfs()

# 결과출력
for low in graph:
    # 요소들을 리스트 형태가 아닌 풀어서 출력
    print(*low)