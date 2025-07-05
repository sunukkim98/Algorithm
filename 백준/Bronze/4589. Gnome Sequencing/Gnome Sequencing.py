import sys
input = sys.stdin.readline

n = int(input().strip())
chk_group = []
for _ in range(n):
    group = list(map(int, input().split()))
    flag = 0
    temp = 0
    chk_order = True
    for num in group:
        if temp == 0:
            temp = num
        else:
            if flag == 0:
                if temp < num:
                    flag = 1
                    temp = num
                else:
                    flag = -1
                    temp = num
            elif flag == 1:
                if temp > num:
                    chk_order = False
            elif flag == -1:
                if temp < num:
                    chk_order = False
    chk_group.append(chk_order)
print("Gnomes:")
for chk in chk_group:
    if chk:
        print("Ordered")
    else:
        print("Unordered")
