import sys
input = sys.stdin.readline

n = int(input().strip())
for _ in range(n):
    word, i, j = input().split()
    i = int(i)
    j = int(j)
    for index in range(len(word)):
        if index < i or index >= j:
            print(word[index], end='')
    print()
