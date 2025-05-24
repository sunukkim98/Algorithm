import sys
input = sys.stdin.readline

N = input().strip()
cnt_map = {'2': 0,
           '0': 0,
           '1': 0,
           '8': 0}
for i in range(int(len(N))):
    if N[i] == '2' or N[i] == '0' or N[i] == '1' or N[i] == '8':
        cnt_map[N[i]] += 1
    else:
        print(0)
        exit()

for key in cnt_map.keys():
    val = cnt_map[key]
    if val == 0:
        print(1)
        exit()
if cnt_map['2'] == cnt_map['0'] == cnt_map['1'] == cnt_map['8']:
    print(8)
else:
    print(2)