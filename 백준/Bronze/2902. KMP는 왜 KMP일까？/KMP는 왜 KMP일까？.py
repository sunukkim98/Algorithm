import sys
input = sys.stdin.readline

long_name = input().strip()
var = long_name.split('-')
for i in range(len(var)):
    print(var[i][0], end='')