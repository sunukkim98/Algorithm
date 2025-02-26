import sys
input = sys.stdin.readline

'''
문제:
    두 번봇대 A와 B사이에 하나 둘씩 전깃줄을 추가하다 보니 전깃줄이 거로 교차하는 경우가 발생하였다.
    합선의 위험이 있어 이들 중 몇 개의 전깃줄을 없애 전깃줄이 교차하지 않도록 만들려고 한다.
    전깃줄이 전봇대에 연결되는 위치는 전봇대 위에서부터 차례대로 번호가 매겨진다.
    전깃줄의 개수와 전깃줄들이 두 전봇대에 연결되는 위치의 번호가 주어질 때, 남아있는 모든 전깃줄이 서로 교차하지 않게 하기 
    위해 없애야 하는 전깃줄의 최소 개수를 구하는 프로그램을 작성하시오.
'''

'''
입력:
    첫째 줄에는 두 전봇대 사이의 전깃줄의 개수가 주어진다. (0 < N <= 100)
    둘째 줄부터 한 줄에 하나씩 전깃줄이 A전봇대와 연결되는 위치의 번호와 B전봇대와 연결되는 위치의 번호가 차례로 주어진다.
    (0 < A_p, B_p <= 500), 같은 위치에 두 개 이상의 전깃줄이 연결될 수 없다.
'''
N = int(input())
pos_map = dict()
for _ in range(N):
    A_p, B_p = map(int, input().split())
    pos_map[A_p] = B_p
pos_map = dict(sorted(pos_map.items()))
key = list(pos_map.keys())
dp = [1] * N
for i in range(1, len(key)):
    for j in range(0, i):
        if pos_map[key[j]] < pos_map[key[i]]:
            dp[i] = max(dp[i], dp[j] + 1)

'''
출력:
    첫째 줄에 남아있는 모든 전깃줄이 서로 교차하지 않게 하기 위해 없애야 하는 전깃줄의 최소 개수를 출력한다.
'''
print(N - max(dp))