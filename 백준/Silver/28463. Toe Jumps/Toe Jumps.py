import sys
input = sys.stdin.readline

direction = input().strip()
board = [input().strip() for i in range(2)]

if direction == 'E':
    t = ['O.', '.P']
    f = ['.P', 'I.']
    l_z = ['.P', 'O.']
elif direction == 'W':
    t = ['P.', '.O']
    f = ['.I', 'P.']
    l_z = ['.O', 'P.']
elif direction == 'S':
    t = ['.O', 'P.']
    f = ['I.', '.P']
    l_z = ['O.', '.P']
else:
    t = ['.P', 'O.']
    f = ['P.', '.I']
    l_z = ['P.', '.O']

if board == t:
    print("T")
elif board == f:
    print("F")
elif board == l_z:
    print("Lz")
else:
    print("?")
