import sys
input = sys.stdin.readline

k = int(input().strip())
for i in range(k):
    n, b = map(int, input().split())
    code_word = []
    for j in range(n):
        code_word.append(input().strip())
    r = input().strip()
    # print(code_word)
    # print(r)

    cnt = [0 for _ in range(len(code_word))]
    for j in range(len(code_word)):
        for k in range(len(code_word[j])):
            if r[k] != code_word[j][k]:
                cnt[j] += 1
    # print(cnt)
    print(f"Data Set {i + 1}:")
    print(min(cnt))
    print()
