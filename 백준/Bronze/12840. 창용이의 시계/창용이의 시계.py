from sys import stdin

# 현재 시간을 h m s로 주어진다
h, m, s = map(int, stdin.readline().strip().split())

# 쿼리의 개수 q가 주어진다. (1 <= q <= 100,000)
q = int(stdin.readline().strip())

"""
쿼리 T가 1이나 2일 때는 c를 입력으로 받아와서, 시계을 앞이나 뒤로 c초 돌린다
쿼리 T가 3일 때는 조작한 시계의 상황을 h m s의 형태로 출력한다
"""
now = h*3600 + m*60 + s

for _ in range(q):
    query = list(map(int, stdin.readline().split()))
    if query[0] == 3:
        print(f"{now // 3600} {(now % 3600) // 60} {now % 60}")
    else:
        T, seconds = query[0], query[1]
        if T == 1:
            now = (now + seconds) % 86400
        elif T == 2:
            now = (now - seconds) % 86400