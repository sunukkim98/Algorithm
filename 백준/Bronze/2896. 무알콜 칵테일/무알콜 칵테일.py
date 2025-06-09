import sys
input = sys.stdin.readline

# input:
# 구매한 주스의 양 A, B, C
A, B, C = map(int, input().split())
# 칵테일을 만드는데 필요한 각 주스의 비율 I, J, K
I, J, K = map(int, input().split())

ratio_I = float(A / I)
ratio_J = float(B / J)
ratio_K = float(C / K)
# print(min(ratio_I, ratio_J, ratio_K))
divider = min(ratio_I, ratio_J, ratio_K)

print(f"{A - (I * divider):.6f} {B - (J * divider):.6f} {C - (K * divider):.6f}")
