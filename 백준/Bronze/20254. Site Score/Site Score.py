import sys

U_R, T_R, U_0, T_0 = map(int, sys.stdin.readline().strip().split())
result = (56 * U_R) + (24 * T_R) + (14 * U_0) + (6 * T_0)
print(result)