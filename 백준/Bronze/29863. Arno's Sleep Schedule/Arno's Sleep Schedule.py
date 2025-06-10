import sys
input = sys.stdin.readline

sleep_start = int(input().strip())
alarm_time = int(input().strip())

temp_time = 0
if sleep_start > 19 and sleep_start < 24:
    temp_time = 24 - sleep_start
    sleep_time = temp_time + alarm_time
else:
    sleep_time = alarm_time - sleep_start
print(sleep_time)
