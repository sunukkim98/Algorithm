import sys
input = sys.stdin.readline

line = input().split()
for bit in line:
    if bit == '9':
        print('F')
        exit()
print('S')