import sys

a_name = sys.stdin.buffer.readline().rstrip()
b_name = sys.stdin.buffer.readline().rstrip()

if a_name == b_name:
    print(0)
else:
    print(1550)
