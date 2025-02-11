import sys
input = sys.stdin.readline

from collections import deque

def solution(N, tree):
    # tree의 루트는 1
    dq = deque([1])
    
    # 부모 노드들을 저장하기 위한 배열 초기화
    parent = [0] * (N + 1)
    
    while dq:
        now = dq.popleft()
        
        # 루트를 시작으로 모든 트리 레벨순서로 순회하며 부모 노드 저장 배열에 각 부모들 저장
        for i in tree[now]:
            if parent[i] == 0 and i != 1:
                parent[i] = now
                dq.append(i)
    
    # 완성된 부모노드들에 대한 정보 반환
    return parent
'''
입력:
    첫째 줄에 노드의 개수 N (2 <= N <= 100,000)이 주어진다.
    둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.
'''
N = int(input())
tree = dict()

# initialize tree
for i in range(1, N + 1):
    tree[i] = []

for _ in range(N - 1):
    n1, n2 = map(int, input().strip().split())
    tree[n1].append(n2)
    tree[n2].append(n1)

'''
출력:
    첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.
'''
parents = solution(N, tree)
for i in range(2, N + 1):
    print(parents[i])