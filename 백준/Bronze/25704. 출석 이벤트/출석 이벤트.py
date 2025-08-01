import sys
input = sys.stdin.readline

n = int(input().strip())
p = int(input().strip())

if n >= 5 and n < 10:
    p = p - 500
elif n >= 10 and n < 15:
    p = int(min(p-500, p-(p*0.1)))
elif n >= 15 and n < 20:
    p = int(min(p-(p*0.1), p - 2000))
elif n >= 20:
    p = int(min(p - 2000, p - (p * 0.25)))

if p <= 0:
    p = 0

print(p)
