import sys
input = sys.stdin.readline

def reverse(x):
    temp = ""
    for i in range(len(x)-1, -1, -1):
        temp += x[i]
    return temp

x, y = input().split()
x = int(reverse(x))
y = int(reverse(y))
print(int(reverse(str(x + y))))
