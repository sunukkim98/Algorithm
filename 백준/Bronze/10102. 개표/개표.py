import sys
input = sys.stdin.readline

V = int(input().strip())
votes = input().strip()
cnt_A = 0
cnt_B = 0
for i in range(len(votes)):
    if votes[i] == 'A':
        cnt_A += 1
    if votes[i] == 'B':
        cnt_B += 1
if cnt_A > cnt_B:
    print('A')
elif cnt_B > cnt_A:
    print('B')
else:
    print('Tie')