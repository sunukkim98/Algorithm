import sys
input = sys.stdin.readline

A = input().strip()
B = input().strip()

mix = ""
for i in range(len(A)):
    mix += A[i] + B[i]
# print(mix)

while len(mix) > 2:
    temp = ""
    for i in range(len(mix) - 1):
        temp += str((int(mix[i]) + int(mix[i+1])) % 10)
    mix = temp
    # print(mix)
print(mix)
