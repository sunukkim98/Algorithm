import sys
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline
# import math

# 다음 풀 문제: 실버 3

name = input().strip()
letter_cnt = {}
for char in name:
    if char in letter_cnt:
        letter_cnt[char] += 1
    else:
        letter_cnt[char] = 1
# print(letter_cnt)

odd_cnt = 0
odd = []
for key in letter_cnt.keys():
    if letter_cnt[key] % 2 != 0:
        odd_cnt += 1
        odd.append(key)
# print(odd_cnt)
# print(odd)

keys = sorted(list(letter_cnt.keys()))
# print(keys)

if odd_cnt > 1:
    print("I'm Sorry Hansoo")
else:
    res = ""

    for key in keys:
        res += key * (letter_cnt[key] // 2)

    if odd:
        res += odd[0] + res[::-1]
    else:
        res += res[::-1]

    print(res)
