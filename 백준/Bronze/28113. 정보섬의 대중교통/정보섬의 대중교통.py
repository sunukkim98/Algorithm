import sys
input = sys.stdin.readline

N, A, B = map(int, input().split())
if A > B and N <= B:
    print("Subway")
elif A == B and N <= B:
    print("Anything")
else:
    print("Bus")
