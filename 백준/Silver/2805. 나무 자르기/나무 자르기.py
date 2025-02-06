import sys
input = sys.stdin.readline

def binary_search(target, data):
    start = 0
    end = max(data)

    while start <= end:
        mid = (start + end) // 2

        temp = 0
        for i in data:
            if i >= mid:
                temp += i - mid

        if temp >= target:
            start = mid + 1
        else:
            end = mid - 1
    print(end)
    return
'''
입력: 
첫째 줄에 나무의 수 N과 집으로 가져가려고 하는 나무의 길이 M이 주어진다. (1 <= N <= 1,000,000, 1 <= M <= 2,000,000,000)
둘째 줄에는 나무의 높이들이 주어진다.
'''
N, M = map(int, input().split())
heights = list(map(int, input().strip().split()))

'''
출력:
적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 출력한다.
'''
binary_search(M, heights)