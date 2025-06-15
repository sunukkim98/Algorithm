import sys
input = sys.stdin.readline

n = int(input().strip())
next = n * 7
year = 2024
month = 1 + next
if month > 12:
    year += month // 12
    month = month % 12
if month == 0:
    year -= 1
    month = 12
print(year, month)
