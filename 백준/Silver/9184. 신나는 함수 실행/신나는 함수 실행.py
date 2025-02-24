import sys
input = sys.stdin.readline

'''
문제:
    다음과 같은 재귀함수 w(a, b, c)가 있다.
'''
# def w(a, b, c):
#     # a, b, c중 하나라도 0보다 작거나 같다면 1반환
#     if a <= 0 or b <= 0 or c <= 0:
#         return 1
#
#     # a, b, c중 하나라도 20보다 크다면 모두 20으로 설정
#     if a > 20 or b > 20 or c > 20:
#         return w(20, 20, 20)
#
#     # a가 b보다 작고 b가 c보다 작다면
#     if a < b and b < c:
#         return w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
#
#     # 위 경우가 모두 아니라면
#     return w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)

def w_dp(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        return w_dp(20, 20, 20)
    
    if dp[a][b][c]:
        return dp[a][b][c]

    if a < b < c:
        dp[a][b][c] = w_dp(a, b, c - 1) + w_dp(a, b - 1, c - 1) - w_dp(a, b - 1, c)
        return dp[a][b][c]

    dp[a][b][c] = w_dp(a - 1, b, c) + w_dp(a - 1, b - 1, c) + w_dp(a - 1, b, c - 1) - w_dp(a - 1, b - 1, c - 1)
    return dp[a][b][c]

dp = [[[0] * (21) for _ in range(21)] for _ in range(21)]

'''
입력:
    입력은 세 정수 a, b, c로 이루어져 있으며, 한 줄에 하나씩 주어진다.
    입력의 마지막은 -1 -1 -1로 나타내며, 세 정수가 모두 -1인 경우는 입력의 마지막을 제외하면 없다.
'''
while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break

    '''
    출력:
        입력으로 주어진 각각의 a, b, c에 대해서, w(a, b, c)를 출력한다.
    '''
    print(f'w({a}, {b}, {c}) = {w_dp(a, b, c)}')
