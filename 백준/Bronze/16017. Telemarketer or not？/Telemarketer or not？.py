import sys
input = sys.stdin.readline

digit_1 = int(input().strip())
digit_2 = int(input().strip())
digit_3 = int(input().strip())
digit_4 = int(input().strip())

if (digit_1 == 9 or digit_1 == 8) and (digit_2 == digit_3) and (digit_4 == 9 or digit_4 == 8):
    print("ignore")
else:
    print("answer")