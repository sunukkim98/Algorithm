import sys
input = sys.stdin.readline

# 다음 풀 문제: 브론즈 1

a, b = map(int, input().split())

sequence = []
for i in range(1, b+1):
    for j in range(i):
        sequence.append(i)

panel = sequence[a-1:b]
# print(panel)
print(sum(panel))
