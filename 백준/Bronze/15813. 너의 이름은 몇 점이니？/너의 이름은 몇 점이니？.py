import sys
input = sys.stdin.readline

length = int(input().strip())
name = list(input().strip())
ascii_list = []
for i in name:
    ascii_list.append(ord(i) - 64)
print(sum(ascii_list))