import sys
input = sys.stdin.readline

s = input().strip()
words = []
for i in range(len(s)):
    word = s[i:]
    words.append(word)
words.sort()
for word in words:
    print(word)
