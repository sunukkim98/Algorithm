import sys
input = sys.stdin.readline

n = int(input().strip())
out = ""
while n > 0:
    if n > 4:
        out += "V"
        n -= 5
    else:
        out += "I"
        n -= 1
print(out)
