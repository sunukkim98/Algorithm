import sys
input = sys.stdin.readline

line = input().replace("\n", "")
a = int(line[0])
b = int(line[4])
c = int(line[8])
if a + b == c:
    print("YES")
else:
    print("NO")