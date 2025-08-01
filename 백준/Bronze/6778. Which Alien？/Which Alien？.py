import sys
input = sys.stdin.readline

num_antenna = int(input().strip())
num_eyes = int(input().strip())

if num_antenna >= 3 and num_eyes <= 4:
    print("TroyMartian")
if num_antenna <= 6 and num_eyes >= 2:
    print("VladSaturnian")
if num_antenna <= 2 and num_eyes <= 3:
    print("GraemeMercurian")
