import sys
input = sys.stdin.readline

S = input().strip()
if any(char in S for char in 'A'):
    S = S.replace('B', 'A')
    S = S.replace('C', 'A')
    S = S.replace('D', 'A')
    S = S.replace('F', 'A')
elif any(char in S for char in 'B'):
    S = S.replace('C', 'B')
    S = S.replace('D', 'B')
    S = S.replace('F', 'B')
elif any(char in S for char in 'C'):
    S = S.replace('D', 'C')
    S = S.replace('F', 'C')
else:
    temp = ""
    for i in range(len(S)):
        temp += 'A'
    S = temp
print(S)
