import sys
input = sys.stdin.readline

# 다음 풀 문제: 브론즈 2

c = int(input().strip())
res = -1
for _ in range(c):
    line = input().strip()
    for_cnt = line.count("for")
    while_cnt = line.count("while")
    cnt = for_cnt + while_cnt
    if cnt > res:
        res = cnt
print(res)
