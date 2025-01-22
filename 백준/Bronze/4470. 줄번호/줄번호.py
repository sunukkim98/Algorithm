from sys import stdin as stdin

N = int(stdin.readline().strip())
lines = []
for _ in range(N):
    lines.append(stdin.readline().replace('\n', ''))
for i in range(len(lines)):
    print(f'{i + 1}. {lines[i]}')