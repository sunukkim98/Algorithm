import sys
input = sys.stdin.readline

# 다음 풀 문제: 실버 4

def dfs(cnt, m, arr, n):
    # cnt가 m과 같다면 수열을 출력한다.
    if cnt == m:
        print(' '.join(map(str, arr)))
        return
    
    # 1~n 순서대로 수열의 원소가 채워진다. (e.g., n이 3이고 m이 3인 경우:
    #                                     1 1 1 -> 1 1 2 -> 1 1 3 ->
    #                                     1 2 1 -> 1 2 2 -> 1 2 3 ->
    #                                     1 3 1 -> 1 3 2 -> 1 3 3 ->
    #                                     2 1 1 -> 2 1 2 -> 2 1 3 ->
    #                                     ...
    #                                     3 3 1 -> 3 3 2 -> 3 3 3)
    for i in range(1, n + 1):
        arr[cnt] = i
        dfs(cnt + 1, m, arr, n)

# 첫째 줄에 자연수 N과 M이 주어진다.
n, m = map(int, input().split())

# 길이가 m인 수열
arr = [0 for _ in range(m)]

# dfs 재귀 함수
dfs(0, m, arr, n)
