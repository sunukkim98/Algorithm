import sys
input = sys.stdin.readline

n, m = map(int, input().split())
items = {}
for _ in range(n):
    line = input().split()
    items[line[0]] = int(line[1]) * 1.05
# print(items)

cnt = 0
for _ in range(m):
    line = input().split()
    if int(line[1]) > items[line[0]]:
        cnt += 1
# print(goods)
print(cnt)
