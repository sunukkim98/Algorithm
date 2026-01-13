import sys

# next goal: Bronze 2

# input
a, b, c = map(int, sys.stdin.readline().split())

# cnt = 1
# while True:
#     cost = a + (b * cnt)
#     income = (c * cnt)
#     if income > cost:
#         print(cnt)
#         break
#     else:
#         if b >= c:
#             print(-1)
#             break
#         else:
#             cnt += 1

temp = c - b
if temp > 0:
    res = (a // temp) + 1
    print(res)
else:
    print(-1)
