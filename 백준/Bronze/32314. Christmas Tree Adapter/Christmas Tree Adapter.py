import sys
input = sys.stdin.readline

a = int(input().strip())
w, v = map(int, input().split())
candidate_a = w / v
# print(a, candidate_a)
if candidate_a >= a:
    print(1)
else:
    print(0)
