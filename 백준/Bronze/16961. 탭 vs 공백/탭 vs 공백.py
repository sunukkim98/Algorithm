import sys
input = sys.stdin.readline

days = {}
for i in range(1, 367):
    days[i] = []

n = int(input().strip())
duration = list()
for _ in range(n):
    c, s, e = input().split()
    s, e = int(s), int(e)
    duration.append(e - s + 1)
    for i in range(s, e+1):
        days[i].append(c)

cnt = 0
people_cnt = set()
no_fight_cnt = 0
no_fight_people = set()
for i in range(1, 367):
    if len(days[i]) > 0:
        cnt += 1
        people_cnt.add(len(days[i]))
        if days[i].count(('T')) == days[i].count('S'):
            no_fight_cnt += 1
            no_fight_people.add(len(days[i]))
print(cnt)
print(max(people_cnt))
print(no_fight_cnt)
if no_fight_cnt == 0:
    print(0)
else:
    print(max(no_fight_people))
print(max(duration))
