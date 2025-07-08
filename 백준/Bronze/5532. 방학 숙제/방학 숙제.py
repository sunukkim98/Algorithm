import sys
input = sys.stdin.readline
import math

L = int(input().strip())
A = int(input().strip())
B = int(input().strip())
C = int(input().strip())
D = int(input().strip())
free_day = L - max(math.ceil(A / C), math.ceil(B / D))
print(free_day)
