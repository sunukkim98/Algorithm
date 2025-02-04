import sys
input = sys.stdin.readline

word = input().strip()
for i in range(len(word)):
    if word[i].isupper():
        print(word[i].lower(), end='')
    else:
        print(word[i].upper(), end='')