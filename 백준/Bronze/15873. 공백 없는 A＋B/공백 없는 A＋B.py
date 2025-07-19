import sys
input = sys.stdin.readline

ab = input().strip()

if ab[1] == '0':
    a = int(ab[:2])
    b = int(ab[2:])
else:
    a = int(ab[0])
    b = int(ab[1:])
print(a + b)
