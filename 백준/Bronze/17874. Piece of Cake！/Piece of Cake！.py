import sys
input = sys.stdin.readline

'''
문제:
    4개의 직사각형 조각으로 잘라진 케잌조각중 4명 중 한 명인 Greg가 가장 큰 케잌 조각을 받을 수 있도록 
    가장 큰 조각의 부피를 출력하라.     
'''

n, h, v = map(int, input().split())

height = 4
if n - h > n // 2:
    h = n - h
# print(h)
if n - v > n // 2:
    v = n - v
# print(v)
print(height * h * v)