import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [i for i in range(1, n+1)]

ans = []
num = 0

for i in range(n):
    num += k - 1
    if num >= len(arr):
        num = num % len(arr)
    ans.append(str(arr.pop(num)))

print("<", ", ".join(ans)[:], ">", sep='')
