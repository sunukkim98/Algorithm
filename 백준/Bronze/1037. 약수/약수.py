import sys
input = sys.stdin.readline

num_of_divider = int(input())
dividers = list(map(int, input().split()))
greatest = max(dividers)
lowest = min(dividers)
print(greatest * lowest)