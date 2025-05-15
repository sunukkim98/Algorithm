import sys
input = sys.stdin.readline

T, F, S, P, C = map(int, input().split())
T_h, F_h, S_h, P_h, C_h = map(int, input().split())

visiting_team = (T * 6) + (F * 3) + (S * 2) + (P) + (C * 2)
home_team = (T_h * 6) + (F_h * 3) + (S_h * 2) + (P_h) + (C_h * 2)
print(visiting_team, home_team)