import sys
input = sys.stdin.readline

t = int(input().strip())
for i in range(1, t+1):
    dice_1, dice_2 = map(int, input().split())
    print(f"Case {i}: {dice_2 + dice_1}")