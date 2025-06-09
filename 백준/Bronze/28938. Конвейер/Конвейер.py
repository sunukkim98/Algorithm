import sys
input = sys.stdin.readline

n = int(input().strip())
order = list(map(int, input().split()))
# print(order)
result = 0
for i in range(len(order)):
    result += order[i]
if result > 0:
    print("Right")
elif result == 0:
    print("Stay")
else:
    print("Left")
