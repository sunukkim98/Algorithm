import sys
input = sys.stdin.readline

# 다음 풀 문제: 브론즈 1

n = int(input().strip())

cnt = 0
current = -1
while True:
    if n == current:
        break
    if current == -1:
        current = n
    # print(current)
    sum = ((current // 10) + (current % 10)) % 10
    current = sum + ((current % 10) * 10)
    # print(current)
    cnt += 1
print(cnt)
