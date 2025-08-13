import sys
input = sys.stdin.readline

# 다음 풀 문제: 브론즈 2

# 16 + 9 + 4 + 1

p = int(input().strip())
for _ in range(p):
    l = int(input().strip())
    total = 0
    for i in range(1, l+1):
        total += i ** 2
    print(total)
