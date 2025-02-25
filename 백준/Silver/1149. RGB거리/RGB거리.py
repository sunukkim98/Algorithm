import sys
input = sys.stdin.readline

'''
문제: 
    RGB거리에는 집이 N개 있다.
    거리는 선분으로 나타낼 수 있고, 1번 집부터 N번 집이 순서대로 있다.
    집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다. 
    각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때, 아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.
    - 1번 집의 색은 2번 집의 색과 같지 않아야 한다.
    - N번 집의 색을 N-1번 집의 색과 같지 않아야 한다.
    - i(2 <= i < N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.
'''

'''
입력:
    첫째 줄에 집의 수 N(2 <= N <= 1,000)이 주어진다. 
    둘째 줄부터 N개의 줄에는 각 집을 빨강, 초록, 파랑으로 칠하는 비용이 1번 집부터 한 줄에 하나씩 주어진다.
    집을 칠하는 비용은 1,000보다 작거나 같은 자연수이다.
'''
N = int(input())
cost_list = []
for _ in range(N):
    cost = map(int, input().split())
    cost_list.append(list(cost))

# cost_list[1][0] = cost_list[1][0] + min(cost_list[0][1], cost_list[0][2])
# cost_list[1][1] = cost_list[1][1] + min(cost_list[0][0], cost_list[0][2])
# cost_list[1][2] = cost_list[1][2] + min(cost_list[0][0], cost_list[0][1])

for i in range(1, N):
    cost_list[i][0] = cost_list[i][0] + min(cost_list[i-1][1], cost_list[i-1][2])
    cost_list[i][1] = cost_list[i][1] + min(cost_list[i-1][0], cost_list[i-1][2])
    cost_list[i][2] = cost_list[i][2] + min(cost_list[i-1][0], cost_list[i-1][1])

'''
출력:
    첫째 줄에 모든 집을 칠하는 비용의 최솟값을 출력한다.
'''
print(min(cost_list[N-1]))