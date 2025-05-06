import sys
input = sys.stdin.readline

graph = [[] for _ in range(11)]

def solve(a, b, c):
    for i in range(1, 11):
        for j in range(1, 11):
            if a * i + b * j == c:
                graph[i].append(j)

        if len(graph[i]) == 0:
            graph[i].append(0)


a, b, c = map(int, input().split())

solve(a, b, c)

for i in range(1, 11):
    for j in range(len(graph[i])):
        print(graph[i][j], end=' ')
    print()