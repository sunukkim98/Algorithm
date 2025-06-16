import sys
# input = sys.stdin.readline

while True:
    try:
        s = input()
    except EOFError:
        break
    print(s)
