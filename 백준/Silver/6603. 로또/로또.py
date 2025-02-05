import sys
input = sys.stdin.readline

from itertools import combinations as C

'''
입력:
각 테스트 케이스는 한 줄로 이루어져 있다. 첫 번째 수는 k (6 < k < 13)
다음 k개 수는 집합 S에 포함되는 수. S의 원소는 오름차순으로 주어진다.
입력의 마지막 줄에는 0이 하나 주어진다.
'''
while True:
    line = input().strip().split()
    k = line[0]
    if k == '0':
        exit()
    k = int(k)
    S = list(map(int, line[1:]))

    '''
    출력:
    각 테스트 케이스마다 수를 고르는 모든 방법을 출력한다.
    사전 순으로 출력
    각 테스트 케이스 사이에는 빈 줄을 하나 출력
    '''
    candidates = C(S, 6)
    for i in candidates:
        print(' '.join(map(str, i)))
    print()