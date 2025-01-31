import sys
input = sys.stdin.readline

# 패티의 개수는 치즈의 개수보다 정확히 한 개 더 많아야 한다.
# 패티의 개수 A와 치즈의 개수 B가 공백으로 구분되어 주어진다.
# 승현이가 만들 수 있는 치즈버거의 최대 크기

A, B = map(int, input().split())

# 패티의 개수가 치즈의 개수보다 많은 경우
if A > B:
    print(B + (B + 1))

# 치즈의 개수가 패티의 개수보다 많은 경우
else:
    print(A + (A - 1))