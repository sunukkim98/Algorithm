import sys
input = sys.stdin.readline

A_att, A_hp = map(int, input().split())
B_att, B_hp = map(int, input().split())
while A_hp > 0 and B_hp > 0:
    A_hp -= B_att
    B_hp -= A_att
if A_hp > 0:
    print("PLAYER A")
elif B_hp > 0:
    print("PLAYER B")
else:
    print("DRAW")
