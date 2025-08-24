import sys
input = sys.stdin.readline
from collections import deque

# 다음 풀 문제: 실버 3

# 1021번 회전하는 큐

# 첫째 줄에 큐의 크기 N과 뽑아내려고 하는 수의 개수 M이 주어진다.
n, m = map(int, input().split())
# 둘째 줄에는 지민이가 뽑아내려고 하는 수의 위치가 순서대로 주어진다.
idxs = list(map(int, input().split()))

# 크기가 n인 deque을 생성한다.
element = []
for i in range(1, n+1):
    element.append(i)
q = deque(element)

cnt = 0
for idx in idxs:
    while True:
        if q[0] == idx:
            q.popleft()
            break
        else:
            if q.index(idx) <= len(q) // 2:
                q.rotate(-1)
                cnt += 1
            else:
                q.rotate(1)
                cnt += 1
print(cnt)
