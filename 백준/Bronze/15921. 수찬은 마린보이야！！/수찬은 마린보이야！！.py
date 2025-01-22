from sys import stdin as stdin

N = int(stdin.readline().strip())
if N == 0:
    print('divide by zero')
    exit()

practice_log = map(int, stdin.readline().strip().split())
total = 0
expect_vals = []
for log in practice_log:
    total += log
    expect_vals.append(log * (1 / N))
expect_val = 0
for val in expect_vals:
    expect_val += val
average = total / N

if N == 0 or expect_val == 0:
    print('divide by zero')
    exit()

result = average/expect_val
result = round(result, 2)
print(f'{result:.2f}')