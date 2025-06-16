import sys
input = sys.stdin.readline

numbers = list(map(int, input().split()))
numbers.sort()
for i in range(len(numbers)):
    print(numbers[i], end=' ')
