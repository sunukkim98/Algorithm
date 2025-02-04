import sys
input = sys.stdin.readline

def check_and_divide(paper, x, y, N):
    first_color = paper[x][y]

    # Check
    for i in range(x, x + N):
        for j in range(y, y + N):
            if paper[i][j] != first_color:
                # Divide
                check_and_divide(paper, x, y, N // 2) # left top
                check_and_divide(paper, x, y + N // 2, N // 2) # right top
                check_and_divide(paper, x + N // 2, y, N // 2) # left bottom
                check_and_divide(paper, x + N // 2, y + N // 2, N // 2) # right bottom
                return
    if first_color == '0':
        result.append(0)
    else:
        result.append(1)

def print_paper(paper):
    for row in paper:
        print(*row)

# 첫째 줄에는 전체 종이의 한 변의 길이 N이 주어져 있다. N = 2, 4, 8, 16, 32, 64, 128 중 하나
N = int(input())

# 색종이의 각 가로줄의 정사각형들의 색이 윗줄부터 차례로 둘째 줄부터 마지막 줄까지 주어진다. 하얀색 = 0, 파란색 = 1 공백으로 구분
paper = [list(input().strip().split()) for _ in range(N)]

# 분할 정복을 사용해 4개의 종이로 나누어가며 전부 같은 색인지 확인이 필요
result = []
check_and_divide(paper, 0, 0, N)

'''
출력:
첫째 줄에는 하얀색 색종이의 개수를 출력
둘째 줄에는 파란색 색종이의 개수를 출력
'''
print(result.count(0))
print(result.count(1))