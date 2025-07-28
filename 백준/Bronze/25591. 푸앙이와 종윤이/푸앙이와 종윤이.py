import sys
input = sys.stdin.readline

input_1, input_2 = map(int, input().split())
a = 100 - input_1
b = 100 - input_2
c = 100 - (a + b)
d = a * b
q = d // 100
r = d % 100
print(a, b, c, d, q, r)
print(c + q, r)
