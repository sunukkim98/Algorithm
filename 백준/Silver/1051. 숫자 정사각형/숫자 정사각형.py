import sys
input = sys.stdin.readline

# 다음 풀 문제: 실버 3

# 1051번 숫자 정사각형

# 첫째 줄에 N과 M이 주어진다. N과 M은 50보다 작거나 같은 자연수이다.
n, m = map(int, input().split())
rectangle = []

# 둘째 줄부터 N개의 줄에 수가 주어진다.
for _ in range(n):
    str_num = input().strip()
    nums = []
    for i in range(m):
        nums.append(int(str_num[i]))
    rectangle.append(nums)

# print(rectangle)

max_len = min(n, m) - 1
# print(max_len)

flag = False

while True:
    if flag:
        break
    for i in range(n - max_len):
        for j in range(m - max_len):
            # print(i, j)
            # print(rectangle[i][j], rectangle[i][j+max_len], rectangle[i+max_len][j], rectangle[i+max_len][j+max_len])
            if rectangle[i][j] == rectangle[i][j+max_len] == rectangle[i+max_len][j] == rectangle[i+max_len][j+max_len]:
                flag = True
                break
    if not flag:
        max_len -= 1

print((max_len + 1) ** 2)
