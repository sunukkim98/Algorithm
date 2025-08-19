import sys
input = sys.stdin.readline

# 다음 풀 문제: 실버 5

num_cnt = {
    '0': 0,
    '1': 0,
    '2': 0,
    '3': 0,
    '4': 0,
    '5': 0,
    '6': 0,
    '7': 0,
    '8': 0,
    '9': 0
}

n = input().strip()

for num in n:
    num_cnt[num] += 1

cnt = []
for i in range(len(num_cnt)):
    cnt.append(num_cnt[str(i)])
if (cnt[6] + cnt[9]) % 2 == 0:
    cnt.append((cnt[6] + cnt[9]) // 2)
else:
    cnt.append(((cnt[6] + cnt[9]) // 2) + 1)
# print(cnt)
cnt[6] = 0
cnt[9] = 0
# print(cnt)
print(max(cnt))

