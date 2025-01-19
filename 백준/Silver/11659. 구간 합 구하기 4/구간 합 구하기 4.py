from sys import stdin as stdin

def get_sum(numbers):
    set_of_sum = [0]
    sum = 0
    for number in numbers:
        sum += int(number)
        set_of_sum.append(sum)
    return set_of_sum

def get_interval_sum(set_of_sum, i, j):
    interval_sum = (set_of_sum[j] - set_of_sum[i-1])
    return interval_sum

# 첫째 줄에 수의 개수 N과 합을 구해야 하는 횟수 M이 주어진다.
N, M = map(int, stdin.readline().strip().split())

# 둘째 줄에는 N개의 수가 주어진다. (수는 1,000보다 작거나 같은 자연수)
numbers = stdin.readline().strip().split()

set_of_sum = get_sum(numbers)
# print(set_of_sum)

# 셋째 줄부터 M개의 줄에는 합을 구해야 하는 구간 i와 j가 주어진다.
for _ in range(M):
    i, j = map(int, stdin.readline().strip().split())
    # print(i, j)
    print(get_interval_sum(set_of_sum, i, j))