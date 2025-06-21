import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

increase_arr = []
for i in range(n):
    tmp = []
    for j in range(m):
        tmp.append(i + j + 1)
    increase_arr.append(tmp)

if increase_arr[n-1][m-1] <= k:
    print("YES")
    for i in increase_arr:
        print(" ".join(map(str, i)))
else:
    print("NO")
