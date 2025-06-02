import sys
input = sys.stdin.readline

HH, MM = map(int, input().split())
H_to_M = (HH - 9) * 60
print(H_to_M + MM)