import sys
input = sys.stdin.readline

lambda_ = int(input().strip())
if lambda_ >= 620 and lambda_ <= 780:
    print("Red")
elif lambda_ >= 590 and lambda_ < 620:
    print("Orange")
elif lambda_ >= 570 and lambda_ < 590:
    print("Yellow")
elif lambda_ >= 495 and lambda_ < 570:
    print("Green")
elif lambda_ >= 450 and lambda_ < 495:
    print("Blue")
elif lambda_ >= 425 and lambda_ < 450:
    print("Indigo")
elif lambda_ >= 380 and lambda_ < 425:
    print("Violet")
