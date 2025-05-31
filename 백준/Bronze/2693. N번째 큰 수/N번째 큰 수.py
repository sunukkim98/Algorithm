import sys
input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    print(arr[2])
