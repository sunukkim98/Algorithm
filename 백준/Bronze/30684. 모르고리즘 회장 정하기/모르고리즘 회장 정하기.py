import sys
input = sys.stdin.readline

N = int(input().strip())
candidate = []
for _ in range(N):
    name = input().strip()
    if len(name) == 3:
        candidate.append(name)
# print(candidate)
candidate.sort()
print(candidate[0])
