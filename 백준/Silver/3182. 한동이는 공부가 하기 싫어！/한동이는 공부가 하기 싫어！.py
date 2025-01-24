from sys import stdin
input = stdin.readline

# 입력의 첫 줄에는 정수 N이 주어진다 (2 <= N <= 1,000)
N = int(input())

# node는 1부터 시작하므로 0번 idx는 사용하지 않음
graph = [0]
result = [0]

# 단방향 그래프로 처리
for i in range(1, N+1):
    graph.append(int(input()))

def dfs(v): # 시작 노드는 v
    # 탐색을 시작하는 노드를 방문으로 처리
    visit[v] = True

    # 노드 v가 가르키는 노드가 방문되지 않았다면 탐색
    if not visit[graph[v]]:
        dfs(graph[v])

# 모든 노드에 대해서 반복
for i in range(1, N+1):
    visit = [False] * (N + 1)

    # 모든 노드를 시작점으로 dfs탐색
    dfs(i)

    # 결과에 방문된 노드 추가
    result.append(visit.count(True))

# 방문한 노드가 가장 많은 시작점 노드 출력
print(result.index(max(result)))