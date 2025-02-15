import sys
input = sys.stdin.readline

N = int(input().strip())
res_arr = list()
for _ in range(N):
    line = input().strip()
    line = list(line)
    line[0] = line[0].upper()
    res_arr.append(''.join(line))
for res in res_arr:
    print(res)