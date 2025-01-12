# 기차들 속도가 다 같다고 가정하면
# 출발순서대로 역에 도착하니까 자기가 탄거 바로 다음 출발시간인 기차로 갈아탐

import sys

# 첫째 줄에 기차의 종류 개수 T(< 30),
# 사장이 출발하는 시간(분 단위로) M(< 60),
# N(<1,000,000,000)번 역이 주어진다.
info = sys.stdin.readline().strip().split()
n = int(info[0])
start_time = int(info[1])
destination = int(info[2])

# 다음 줄에는 각 기차 종류별로 기차의 번호(길이 10을 넘지 않는 문자열)과
# 그 기차가 0번 역에서 출발하는 시간을 분 단위(<60)로 입력한다. 각 줄의 끝에는 -1로 주어진다.
trains = []
for _ in range(n):
    line = sys.stdin.readline().strip().split()
    name = line[0]
    times = list(map(int, line[1:-1]))

    for time in times:
        trains.append([time, name])

# 도착시간에 따른 기차정보 정렬
trains.sort(key=lambda x: x[0])

# 첫 출발 기차는 출발시간과 같거나 이후 도착하는 기차
start_index = 0
for i, (time, _) in enumerate(trains):
    if time >= start_time:
        start_index = i
        break

# n번째 역에 도착할 기차정보 = 기차정보들[((정렬된 기차정보의 첫 출발 기차 idx) + (n % 기차의 종류들(도착시간이 다르면 다른 열차)) + (기차의 종류들 - 1)) % 기차의 종류들]
remainder = destination % len(trains)
final_index = (start_index + remainder + len(trains) - 1) % len(trains)
solution = trains[final_index][1]

print(solution)
