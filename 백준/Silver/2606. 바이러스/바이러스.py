import sys
from collections import defaultdict

def dfs_recursive(graph, start, visited = []):
    visited.append(start)

    for node in graph[start]:
        if node not in visited:
            dfs_recursive(graph, node, visited)
    return visited

def make_graph(nodes, edges):
    graph = defaultdict(list)
    for node in nodes:
        for edge in edges:
            if edge[0] == node:
                graph[node].append(edge[1])
    return graph

# 첫째 줄에는 컴퓨터의 수가 주어진다.(0 <= n <= 100)
n = int(sys.stdin.readline().strip())
nodes = []
for i in range(1, n + 1): # * 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다.
    nodes.append(i)
# print(nodes)

# 둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다.
n_edges = int(sys.stdin.readline().strip())

# 이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.
edges = []
for _ in range(n_edges):
    src, dst = map(int, sys.stdin.readline().strip().split())
    edges.append([src, dst])
    edges.append([dst, src])
# print(edges)
graph = make_graph(nodes, edges)
# print(graph)

# 출력: 1번 컴퓨터가 웜 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 첫째 출에 출력
print(len(dfs_recursive(graph,1)) - 1)


