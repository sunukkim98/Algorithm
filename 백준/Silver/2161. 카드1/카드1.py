import sys
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline
# import math
from collections import deque

# 다음 풀 문제: 실버 5

# 2161번 카드 1

# 첫째 줄에 정수 N(1 ≤ N ≤ 1,000)이 주어진다.
n = int(input().strip())

# 순서가 1, 2, ..., N인 리스트를 생성한다.
cards = [i for i in range(1, n+1)]

# cards 리스트를 덱 자료형으로 변환한다.
cards = deque(cards)

# 가장 처음 숫자는 pop하여 결과 리스트에 추가, 그 다음 숫자는 cards 큐의 뒤에 추가한다.
while True:
    if len(cards) == 0:
        break
    elif len(cards) == 1:
        print(cards.popleft(), end='')
    else:
        print(cards.popleft(), end=' ')
        temp = cards.popleft()
        cards.append(temp)