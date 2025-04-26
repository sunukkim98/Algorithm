import sys

input = sys.stdin.readline

beer, malt, wine, soft_drinks, seltzer, water = map(int, input().split())

beer *= 5
malt *= 5
wine *= 5
soft_drinks *= 5
seltzer *= 5
water *= 5

print(beer + malt + wine + soft_drinks + seltzer + water)