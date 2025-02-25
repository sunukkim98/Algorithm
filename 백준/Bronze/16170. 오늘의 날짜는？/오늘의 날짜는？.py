import sys
input = sys.stdin.readline

import datetime

'''
문제:
    지금 시각을 기준으로 나타냈을 때의 연도, 월, 일을 한 줄에 하나씩 순서대로 출력한다.
'''
now = datetime.datetime.now()
year = now.strftime("%Y")
month = now.strftime("%m")
day = now.strftime("%d")
print(year)
print(month)
print(day)