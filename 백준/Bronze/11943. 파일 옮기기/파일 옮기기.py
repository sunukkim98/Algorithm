import sys
input = sys.stdin.readline

a, b = map(int, input().split())
c, d = map(int, input().split())
case_1 = a + d
case_2 = b + c
print(min(case_1, case_2))
