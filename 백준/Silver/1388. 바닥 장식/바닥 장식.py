import sys
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline
# import math
# from collections import deque

# 다음 풀 문제: 실버 3

# 1388번 바닥 장식

def print_map(map, n, m):
    for i in range(n):
        for j in range(m):
            print(map[i][j], end='')
        print()

# 첫째 줄에 방 바닥의 세로 크기N과 가로 크기 M이 주어진다. N과 M은 50 이하인 자연수이다.
n, m = map(int, input().split())

# 둘째 줄부터 N개의 줄에 M개의 문자가 주어진다. 이것은 바닥 장식 모양이고, '-‘와 ’|‘로만 이루어져 있다.
map = []
for _ in range(n):
    map.append(list(input().strip()))

# print_map(map, n, m)

cnt = 0

for i in range(n):
    for j in range(m):
        if map[i][j] == '-':
            # print("check row!")
            map[i][j] = 'x'
            for k in range(j + 1, m):
                if map[i][k] == '-':
                    map[i][k] = 'x'
                else:
                    break
            cnt += 1
        elif map[i][j] == '|':
            # print("check column!")
            map[i][j] = 'x'
            for k in range(i + 1, n):
                if map[k][j] == '|':
                    map[k][j] = 'x'
                else:
                    break
            cnt += 1

# 첫째 줄에 문제의 정답을 출력한다.
print(cnt)
