import sys
input = sys.stdin.readline

a, b = map(int, input().split())
k, x = map(int, input().split())
start = max(a, k - x)
end = min(b, k + x)
# print(start, end)
if end - start + 1 <= 0:
    print("IMPOSSIBLE")
else:
    print(end - start + 1)
