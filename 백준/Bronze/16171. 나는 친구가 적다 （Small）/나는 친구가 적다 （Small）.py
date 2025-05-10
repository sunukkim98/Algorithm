import sys
input = sys.stdin.readline

S = input().strip()
K = input().strip()

S_strip = ''.join(char for char in S if not char.isnumeric())
# print(S_strip)

if K in S_strip:
    print(1)
else:
    print(0)