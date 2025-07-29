import sys
input = sys.stdin.readline

n = int(input().strip())
for i in range(1, n+1):
    line = list(map(int, input().split()))
    print(f"Case #{i}: {max(line)}")
