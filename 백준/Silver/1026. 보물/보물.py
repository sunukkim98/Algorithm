import sys
input = sys.stdin.readline

n = int(input().strip())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
# print(a)

temp = b.copy()
idx_list = []
for i in range(n):
    # print(temp.index(max(temp)))
    idx = temp.index(max(temp))
    idx_list.append(idx)
    temp[idx] = -1

# print(b)
# print(temp)
# print(idx_list)

temp_a = a.copy()
for idx in idx_list:
    a[idx] = temp_a[0]
    del temp_a[0]
# print(a)

res = 0
for i in range(n):
    res += a[i] * b[i]
print(res)
