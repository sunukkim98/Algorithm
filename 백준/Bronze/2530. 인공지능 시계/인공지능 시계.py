c_h, c_m, c_s = map(int, input().split())
time_for_cook = int(input())
p_h = time_for_cook // 3600
p_m = (time_for_cook % 3600) // 60
p_s = (time_for_cook % 3600) % 60
if c_s + p_s >= 60:
    p_m += 1
    p_s -= 60
if c_m + p_m >= 60:
    p_h += 1
    p_m -= 60
result_hour = c_h + p_h
if result_hour >= 24:
    result_hour %= 24

print(f'{result_hour} {c_m + p_m} {c_s + p_s}')
