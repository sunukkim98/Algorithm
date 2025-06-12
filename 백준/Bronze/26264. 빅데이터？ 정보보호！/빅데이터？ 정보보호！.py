import sys
input = sys.stdin.readline

n = int(input().strip())
line = input().strip()
cnt_s = 0
cnt_b = 0
for i in range(len(line)):
    if line[i] == 's':
        cnt_s += 1
    if line[i] == 'b':
        cnt_b += 1
if cnt_s > cnt_b:
    print("security!")
elif cnt_s == cnt_b:
    print("bigdata? security!")
else:
    print("bigdata?")
