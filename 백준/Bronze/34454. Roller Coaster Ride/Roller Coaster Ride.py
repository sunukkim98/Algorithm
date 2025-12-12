import sys

n = int(sys.stdin.buffer.readline().rstrip())
c = int(sys.stdin.buffer.readline().rstrip())
p = int(sys.stdin.buffer.readline().rstrip())

if n <= c * p:
    print("yes")
else:
    print("no")
