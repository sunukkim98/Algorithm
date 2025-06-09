import sys
input = sys.stdin.readline

n = int(input().strip())
order = list(map(int, input().split()))
# print(order)
even_cnt = 0
odd_cnt = 0
for i in range(len(order)):
    if order[i] % 2 == 0:
        even_cnt += 1
    else:
        odd_cnt += 1
if even_cnt > odd_cnt:
    print("Happy")
else:
    print("Sad")
