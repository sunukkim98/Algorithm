import sys
input = sys.stdin.readline

word = input().strip()
if 'M' in word and 'O' in word and 'B' in word and 'I' in word and 'S' in word:
    print("YES")
else:
    print("NO")
