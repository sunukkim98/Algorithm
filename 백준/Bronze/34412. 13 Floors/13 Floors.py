import sys

x = int(sys.stdin.buffer.readline().rstrip())

if x > 12:
    print(x + 1)
else:
    print(x)
