import sys
input = sys.stdin.readline

x, y = map(int, input().split())
a = ''
for _ in range(x):
    a += '1'
a = int(a)

b = ''
for _ in range(y):
    b += '1'
b = int(b)
print(a + b)
