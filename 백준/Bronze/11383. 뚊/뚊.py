import sys
input = sys.stdin.readline

N, M = map(int, input().split())
chars_M = []
chars_2M = []
temp = ["" for _ in range(N)]
flag = True
for i in range(N):
    chars_M.append(input().strip())
    for j in range(len(chars_M[i])):
        temp[i] += chars_M[i][j]
        temp[i] += chars_M[i][j]
# print(chars_M)
# print(temp)

for i in range(N):
    chars_2M.append(input().strip())
for i in range(N):
    if chars_2M[i] != temp[i]:
        flag = False
if flag:
    print("Eyfa")
else:
    print("Not Eyfa")
