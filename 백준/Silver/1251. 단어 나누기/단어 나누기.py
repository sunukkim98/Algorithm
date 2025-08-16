import sys
input = sys.stdin.readline

# 다음 풀 문제: 실버 5

word = list(input().strip())
ans = []
tmp = []

for i in range(1, len(word)-1):
    for j in range(i+1, len(word)):
        a = word[:i]
        b = word[i:j]
        c = word[j:]
        a.reverse()
        b.reverse()
        c.reverse()
        tmp.append(a + b + c)

for word in tmp:
    ans.append(''.join(word))

print(sorted(ans)[0])
