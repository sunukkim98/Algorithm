import sys
input = sys.stdin.readline

total = int(input().strip())
gap = int(input().strip())
print((total + gap) // 2)
print((total - gap) // 2)
