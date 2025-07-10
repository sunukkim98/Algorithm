import sys
input = sys.stdin.readline

n = int(input().strip())
A = list(map(int, input().split()))
temp = 0
check = True
shape = True
for i in range(n-1):
    if A[i] < A[i+1]:
        if shape == False:
            check = False
            break
    elif A[i] == A[i+1]:
        check = False
        break
    else:
        shape = False

if check:
    print("YES")
else:
    print("NO")
