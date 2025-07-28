import sys
input = sys.stdin.readline

depths = []
for _ in range(4):
    depths.append(int(input().strip()))

is_sorted = (sorted(depths) == depths)
is_reversed = (sorted(depths, reverse=True) == depths)

check_identical = True
for i in range(3):
    if depths[i] == depths[i+1]:
        check_identical = False

if is_sorted:
    if max(depths) == min(depths):
        print("Fish At Constant Depth")
    elif check_identical:
        print("Fish Rising")
    else:
        print("No Fish.")
elif is_reversed and check_identical:
    print("Fish Diving")
else:
    print("No Fish")
