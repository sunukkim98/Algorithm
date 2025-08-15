import sys
input = sys.stdin.readline

# 다음 풀 문제: 브론즈 1

n = int(input().strip())
files = []
for _ in range(n):
    files.append(input().strip())
flags = []
for i in range(len(files[0])):
    flag = True
    for j in range(len(files)):
        for k in range(j+1, len(files)):
            # print(i, j, k)
            # print(files[j][i])
            # print(files[k][i])
            if files[j][i] != files[k][i]:
                flag = False
    flags.append(flag)

res = ""
for i in range(len(flags)):
    if flags[i]:
        res += files[0][i]
    else:
        res += "?"
print(res)
