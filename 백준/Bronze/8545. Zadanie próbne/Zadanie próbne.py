import sys
input = sys.stdin.readline

word = input().strip()
output = ""
for i in range(len(word)-1, -1, -1):
    output += word[i]
print(output)
