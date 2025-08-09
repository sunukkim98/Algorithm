import sys
input = sys.stdin.readline

n = int(input().strip())

suspect = []
for _ in range(n):
    suspect.append(input().strip())
for s in suspect:
    if 'S' in s:
        print(s)
        break
