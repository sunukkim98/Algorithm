import sys
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline
import math

# 다음 풀 문제: 브론즈 2

n = int(input().strip())
letter_cnt = {}
for _ in range(n):
    name = input().strip()
    if name[0] not in letter_cnt:
        letter_cnt[name[0]] = 1
    else:
        letter_cnt[name[0]] += 1

res = []
for key in letter_cnt.keys():
    if letter_cnt[key] >= 5:
        res.append(key)

res.sort()

if len(res) == 0:
    print("PREDAJA")
else:
    print(''.join(res))
