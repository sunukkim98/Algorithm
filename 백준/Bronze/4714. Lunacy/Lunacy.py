import sys
input = sys.stdin.readline

while True:
    weight = float(input().strip())
    if weight == -1:
        break
    # print(weight)
    print(f"Objects weighing {weight:.2f} on Earth will weigh {weight* 0.167:.2f} on the moon.")
