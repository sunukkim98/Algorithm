import sys

# next goal: Bronze 3

# input
n = int(sys.stdin.readline().strip())
sum = 0
for i in range(n):
    j = int(sys.stdin.readline().strip())
    if i == 0:
        sum += j
    else:
        sum += (j-1)
print(sum)
