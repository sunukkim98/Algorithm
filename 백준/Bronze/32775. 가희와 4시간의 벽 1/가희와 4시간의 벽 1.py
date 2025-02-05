import sys
input = sys.stdin.readline

S_ab = int(input())
F_ab = int(input())

if S_ab <= F_ab:
    print('high speed rail')
else:
    print('flight')