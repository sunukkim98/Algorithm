import sys
input = sys.stdin.readline

n, d = map(int, input().split())
num_of_prob = []
total_prob = 0
for i in range(n):
    num_of_prob.append(int(input()))
    total_prob += num_of_prob[i]
d = d // total_prob
for i in range(n):
    print(num_of_prob[i] * d)