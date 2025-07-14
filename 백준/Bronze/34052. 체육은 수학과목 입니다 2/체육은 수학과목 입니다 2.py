import sys
input = sys.stdin.readline

current_time = 0
for _ in range(4):
    current_time += int(input().strip())
if (1800 - current_time) > 299:
    print("Yes")
else:
    print("No")
