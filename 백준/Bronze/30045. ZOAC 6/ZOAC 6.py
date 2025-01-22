from sys import stdin as stdin

N = int(stdin.readline().strip())
lines = []
for _ in range(N):
    lines.append(stdin.readline().strip())
cnt = 0
for line in lines:
    index_01 = line.find('01')
    index_OI = line.find('OI')
    if index_01 != -1 or index_OI != -1:
        cnt += 1
print(cnt)