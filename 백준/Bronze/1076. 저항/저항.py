import sys
input = sys.stdin.readline

# 다음 풀 문제: 브론즈 2

table = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9
}

c1 = input().strip()
c2 = input().strip()
c3 = input().strip()

print((table[c1] * 10 + table[c2]) * 10 ** table[c3])
