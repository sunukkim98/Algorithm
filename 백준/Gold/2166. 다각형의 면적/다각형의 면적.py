import sys
input = sys.stdin.readline

'''
https://oozoowos.tistory.com/entry/%EA%B8%B0%ED%95%98-%EB%8B%A4%EA%B0%81%ED%98%95-%EB%84%93%EC%9D%B4-%EA%B5%AC%ED%95%98%EB%8A%94-%EA%B3%B5%EC%8B%9D
문제: 2166번 다각형의 면적
    2차원 평면상에 N(3 <= N <= 10,000)개의 점으로 이루어진 다각형이 있다. 이 다각형의 면적을 구하는 프로그램을 작성하시오.
'''

'''
입력:
    첫째 줄에 N이 주어진다. 다음 N개의 줄에는 다각형을 이루는 순서대로 N개의 점의 x, y좌표가 주어진다. 좌표값은 절댓값이 100,000을 넘지
    않는 정수이다.
'''
N = int(input())
points = []
for _ in range(N):
    x, y = map(int, input().split())
    points.append([x, y])
points.append(points[0])

x = y = 0
for i in range(1, N + 1):
    x += points[i][1] * points[i-1][0]
    y += points[i][0] * points[i-1][1]

'''
출력:
    첫째 줄에 면적을 출력한다. 면적을 출력할 때에는 소수점 아래 둘째 자리에서 반올림하여 첫째 자리까지 출력한다.
'''
print(round(abs(x-y)) / 2)