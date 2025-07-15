import sys
input = sys.stdin.readline

option_1 = []
for _ in range(4):
    option_1.append(int(input().strip()))

option_2 = []
for _ in range(2):
    option_2.append(int(input().strip()))

option_1.sort(reverse=True)
option_2.sort(reverse=True)

sum_of_score = 0

for i in range(3):
    sum_of_score += option_1[i]
for i in range(1):
    sum_of_score += option_2[i]

print(sum_of_score)
