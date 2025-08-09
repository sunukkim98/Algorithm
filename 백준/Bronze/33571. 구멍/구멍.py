import sys
input = sys.stdin.readline

s = input().strip()
cnt = 0
hole_1 = ['A', 'a', 'b', 'D', 'd', 'e', 'g', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', '@']
hole_2 = ['B']
for c in s:
    if c in hole_1:
        # print(c)
        cnt += 1
    elif c in hole_2:
        # print(c, 2)
        cnt += 2
print(cnt)
