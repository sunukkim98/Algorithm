import sys
# input = sys.stdin.readline

'''
문제:
    재귀적인 패턴으로 별을 찍어 보자. 
    N이 3의 거듭제곱 (3, 9, 27, ...) 이라고 할 때, 크기 N의 패턴은 N * N 정사각형 모양이다.
    크기 3의 패턴은 가운데에 공백이 있고, 가운데를 제외한 모든 칸에 별이 하나씩 있는 패턴이다.
    ***
    * *
    ***
    N이 3보다 클 경우, 크기 N의 패턴은 공백으로 채워진 (N / 3) * (N / 3) 정사각형을 크기 N / 3의 패턴으로 둘러싼
    형태이다.
'''
def recursive_star(N: int):
    if N == 1:
        return ['*']
    stars = recursive_star(N // 3)
    temp = []
    for star in stars:
       temp.append(star * 3)
    for star in stars:
        temp.append(star + ' ' * (N // 3) + star)
    for star in stars:
       temp.append(star * 3)
    return temp

'''
입력:
    첫째 줄에 N이 주어진다. N은 3의 거듭제곱이다. 즉 어떤 상수 k에 대해 N = 3^k이며, 이때 1 <= K < 8이다.
'''
N = int(input())

star = recursive_star(N)
'''
출력:
    첫째 줄부터 N번째 줄까지 별을 출력한다.
'''
for i in range(N):
    for j in range(N):
        print(star[i][j], end='')
    print()