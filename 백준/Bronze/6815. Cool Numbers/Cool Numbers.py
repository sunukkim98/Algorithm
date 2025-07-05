import sys
input = sys.stdin.readline

def pow6(num: int):
    return num * num * num * num * num * num

a = int(input().strip())
b = int(input().strip())
idx = 1
cnt = 0
while pow6(idx) <= b:
    if pow6(idx) >= a:
        cnt += 1
    idx += 1
print(cnt)
