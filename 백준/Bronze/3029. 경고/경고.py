import sys
input = sys.stdin.readline

current_time = input().strip()
throw_time = input().strip()
c_h, c_m, c_s = map(int, current_time.split(':'))
t_h, t_m, t_s = map(int, throw_time.split(':'))

if c_s > t_s:
    t_m -= 1
    s = (t_s + 60) - c_s
else: s = t_s - c_s

if c_m > t_m:
    t_h -= 1
    m = (t_m + 60) - c_m
else: m = t_m - c_m

if c_h > t_h:
    h = (t_h + 24) - c_h
else: h = t_h - c_h

if c_h == t_h and c_m == t_m and c_s == t_s:
    h = 24
    m = 0
    s = 0

hour = str(h)
if len(hour) != 2:
    hour = "0" + hour
min = str(m)
if len(min) != 2:
    min = "0" + min
sec = str(s)
if len(sec) != 2:
    sec = "0" + sec
print(f"{hour}:{min}:{sec}")
