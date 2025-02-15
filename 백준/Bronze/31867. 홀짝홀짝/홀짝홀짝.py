import sys
input = sys.stdin.readline

N = int(input().strip())
K = input().strip()
digits = list()
for i in range(len(K)):
    digits.append(int(K[i]))
even_cnt, odd_cnt = 0, 0
for num in digits:
    if num % 2 == 0:
        even_cnt += 1
    else:
        odd_cnt += 1
if even_cnt > odd_cnt:
    print(0)
elif even_cnt < odd_cnt:
    print(1)
else:
    print(-1)