import sys
input = sys.stdin.readline

n = int(input().strip())
ans = []
response = []
for _ in range(n):
    ans.append(input().strip())
for _ in range(n):
    response.append(input().strip())
cnt = 0
for i in range(len(ans)):
    if ans[i] == response[i]:
        cnt += 1
print(cnt)
