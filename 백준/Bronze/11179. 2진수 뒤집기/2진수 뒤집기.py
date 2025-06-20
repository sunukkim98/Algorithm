import sys
input = sys.stdin.readline

def reverse(x):
    temp = ""
    for i in range(len(x)-1, -1, -1):
        temp += x[i]
    return temp

n = int(input().strip())
bin_n = bin(n)
# print(bin_n)
reverse = reverse(bin_n[2:])
bin_n = bin_n[:2]
bin_n += reverse
print(int(bin_n, 2))

