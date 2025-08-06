import sys
input = sys.stdin.readline

n = int(input().strip())
call_time = list(map(int, input().split()))
# print(call_time)
y = 0
m = 0
for call in call_time:
    # print(((call // 30) + 1) * 10)
    y += ((call // 30) + 1) * 10
    m += ((call // 60) + 1) * 15

# print(y, m)
if y < m:
    print(f"Y {y}")
elif m < y:
    print(f"M {m}")
else:
    print(f"Y M {y}")
