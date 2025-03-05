import sys
input = sys.stdin.readline

from collections import deque

'''
문제: 2667 단지번호붙이기
    <그림 1>  <그림 2>
    0110100  0110200
    0110101  0110202
    1110101  1110202
    0000111  0000222
    0100000  0300000
    0111110  0333330
    0111000  0333000
    <그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 철수는 이 지도를 가지고 연결된 집의
    모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다.
    대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고,
    각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.
'''
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(graph: list(), a: int, b: int):
    '''
    :param graph: input graph
    :param a: row idx
    :param b: col idx
    :return count: 단지에 속하는 집의 수
    '''
    n = len(graph)
    queue = deque()
    queue.append((a, b))
    
    # 0으로 탐색한 노드를 만들어야 재탐색하지 않음
    graph[a][b] = 0

    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 1:
                # 0으로 탐색한 노드를 만들어야 재탐색하지 않음
                graph[nx][ny] = 0
                queue.append((nx, ny))
                
                # 한 단지내의 집의 개수 증가 
                count += 1
    return count

'''
입력: 
    첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 길이는 같으며 5 <= N <= 25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료
    (0혹은 1)가 입력된다.
'''
N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int, input().strip())))

# 단지 내의 집의 개수를 저장할 변수
cnt = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            cnt.append(bfs(graph, i, j))

'''
출력:
    첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.
'''
cnt.sort()
print(len(cnt))
for i in range(len(cnt)):
    print(cnt[i])