import sys

n = int(sys.stdin.readline().strip())

base = 10 ** 8

if (n ** 2) <= base:
    print("Accepted")
else:
    print("Time limit exceeded")
