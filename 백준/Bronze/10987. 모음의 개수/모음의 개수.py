import sys
input = sys.stdin.readline

s = input().strip()
vowel_cnt = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
for i in range(len(s)):
    # print(s[i])
    if s[i] in vowel_cnt.keys():
        vowel_cnt[s[i]] += 1
# print(vowel_cnt)

res = 0
for cnt in vowel_cnt.values():
    res += cnt
print(res)
