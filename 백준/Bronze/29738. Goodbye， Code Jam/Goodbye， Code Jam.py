import sys
input = sys.stdin.readline

t = int(input().strip())
for i in range(t):
    rank = int(input().strip())
    if rank <= 25:
        print(f"Case #{i+1}: World Finals")
    elif rank <= 1000:
        print(f"Case #{i+1}: Round 3")
    elif rank <= 4500:
        print(f"Case #{i+1}: Round 2")
    else:
        print(f"Case #{i + 1}: Round 1")
