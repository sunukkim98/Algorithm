import sys
input = sys.stdin.readline

k = int(input().strip())
for i in range(k):
    C, B, n, r = map(int, input().split())

    bailed_company = list(map(int, input().split()))
    assert B == len(bailed_company), 'len mismatch'

    total = 0
    for j in range(n):
        c_i, p_i = map(int, input().split())
        if c_i in bailed_company:
            ratio = r / 100
            total += int(p_i * ratio)
    print(f"Data Set {i+1}:")
    print(total)
    print()
