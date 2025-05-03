import sys
input = sys.stdin.readline

import operator

seminars = dict()

for i in range(7):
    name, num = input().split()
    seminars[name] = int(num)

seminars = sorted(seminars.items(), key=operator.itemgetter(1), reverse=True)
print(seminars[0][0])