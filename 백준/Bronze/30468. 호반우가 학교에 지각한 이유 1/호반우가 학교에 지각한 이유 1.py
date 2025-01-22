from sys import stdin as stdin

STR, DEX, INT, LUK, N = map(int, stdin.readline().strip().split())
total_stats = STR + DEX + INT + LUK
cnt = 0
while total_stats / 4 < N:
    total_stats += 1
    cnt += 1
print(cnt)