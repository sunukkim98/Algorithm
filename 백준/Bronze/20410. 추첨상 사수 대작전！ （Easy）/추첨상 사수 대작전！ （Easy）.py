import sys
input = sys.stdin.readline

'''
입력:
    한 줄에 걸쳐 준표가 좋아하는 소수 m, 참가자들이 정한 Seed, 시연으로 공개된 X_1, X_2이 주어진다.
'''
m, Seed, X_1, X_2 = map(int, input().strip().split())

for i in range(m):
    for j in range(m):
        if X_1 == ((i * Seed) + j) % m and X_2 == ((i * X_1) + j) % m:
            print(i, j)
            exit()