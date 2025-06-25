import sys
input = sys.stdin.readline

n = input().strip()
f = int(input().strip())

start = n[:-2]
start += "00"
start = int(start)
# print(start)

for i in range(start, start + 100):
    if i % f == 0:
        print(str(i)[-2:])
        break
