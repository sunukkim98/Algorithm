import sys
input = sys.stdin.readline

n = int(input().strip())
s = input().strip()
o_cnt = 0
for i in range(len(s)):
    if s[i] == 'O':
        o_cnt += 1

condition = n // 2
if n % 2 == 0:
    condition = n // 2
else:
    condition = (n // 2) + 1

if o_cnt >= condition:
    print("Yes")
else:
    print("No")
