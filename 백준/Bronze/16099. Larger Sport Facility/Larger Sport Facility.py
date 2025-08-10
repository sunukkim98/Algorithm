import sys
input = sys.stdin.readline

n = int(input().strip())
for _ in range(n):
    l_t, w_t, l_e, w_e = map(int, input().split())
    if l_t * w_t > l_e * w_e:
        print("TelecomParisTech")
    elif l_t * w_t < l_e * w_e:
        print("Eurecom")
    else:
        print("Tie")
