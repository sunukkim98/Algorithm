import sys
input = sys.stdin.readline

bowl_weight = []
for i in range(3):
    bowl_weight.append(int(input().strip()))
bowl_weight.sort()
print(bowl_weight[1])