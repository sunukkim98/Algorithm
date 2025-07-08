import sys
input = sys.stdin.readline

n = int(input().strip())
for i in range(1, n+1):
    length = list(map(int, input().split()))
    max_length = max(length)
    length.remove(max_length)
    print(f"Scenario #{i}:")
    if max_length * max_length == length[0] * length[0] + length[1] * length[1]:
        print("yes")
    else:
        print("no")
    print()
