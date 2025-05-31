import sys
input = sys.stdin.readline

N = int(input().strip())
S = input().strip()
cnt = 0
for i in range(len(S)):
    if S[i] == 'a' or S[i] == 'i' or S[i] == 'u' or S[i] == 'e' or S[i] == 'o':
        cnt += 1
print(cnt)