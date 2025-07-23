import sys
input = sys.stdin.readline

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b / gcd(a, b)

n = int(input().strip())
for _ in range(n):
    a, b = map(int, input().split())

    res = lcm(a, b)
    print(int(res))
