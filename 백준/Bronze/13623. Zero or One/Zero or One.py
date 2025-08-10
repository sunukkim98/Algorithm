import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
cnt_0 = 0
cnt_1 = 0
if a == 0:
    cnt_0 += 1
else:
    cnt_1 += 1
if b == 0:
    cnt_0 += 1
else:
    cnt_1 += 1
if c == 0:
    cnt_0 += 1
else:
    cnt_1 += 1

if cnt_0 == 0 or cnt_1 == 0:
    print("*")
else:
    if cnt_0 == 1:
        if a == 0:
            print("A")
        elif b == 0:
            print("B")
        else:
            print("C")
    else:
        if a == 1:
            print("A")
        elif b == 1:
            print("B")
        else:
            print("C")
