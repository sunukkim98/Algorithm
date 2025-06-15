import sys
input = sys.stdin.readline

uos = "UOS"
x = int(input().strip())
x %= 3
print(uos[x-1])
