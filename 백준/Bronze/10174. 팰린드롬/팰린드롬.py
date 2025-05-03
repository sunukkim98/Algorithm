import sys
input = sys.stdin.readline

n = int(input().strip())
for i in range(n):
    line = input().strip().lower()
    # line = line.replace(' ', '')
    # print(line)
    last = len(line) - 1
    flag = True
    for j in range(len(line) // 2):
        # print(line[j], line[last])
        if line[j] != line[last]:
            flag = False
            break
        last -= 1
    if flag == True:
        print("Yes")
    else:
        print("No")