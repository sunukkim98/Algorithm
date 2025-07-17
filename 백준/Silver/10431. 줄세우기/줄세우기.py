import sys
input = sys.stdin.readline

p = int(input().strip())
for _ in range(p):
    line = list(map(int, input().split()))
    t = line[0]
    heights = line[1:]
    step = 0
    res = []

    for height in heights:
        res.append(height)
        if sorted(res) != res:
            step += res.index(height)
            res.sort()
            step -= res.index(height)
    print(t, step)
