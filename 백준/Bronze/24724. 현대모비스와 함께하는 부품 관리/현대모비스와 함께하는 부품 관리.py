import sys

# next goal: Bronze 4

# input
t = int(sys.stdin.readline().strip())

for i in range(t):
    n = int(sys.stdin.readline().strip())
    a, b = map(int, sys.stdin.readline().split())
    for j in range(n):
        u_i, v_i = map(int, sys.stdin.readline().split())
    print(f"Material Management {i+1}")
    print(f"Classification ---- End!")
