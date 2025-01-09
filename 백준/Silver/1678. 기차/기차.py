# 첫째 줄에 기차의 종류 개수 T(< 30),
# 사장이 출발하는 시간(분 단위로) M(< 60),
# N(<1,000,000,000)번 역이 주어진다.
# 다음 줄에는 각 기차 종류별로 기차의 번호(길이 10을 넘지 않는 문자열)과
# 그 기차가 0번 역에서 출발하는 시간을 분 단위(<60)로 입력한다. 각 줄의 끝에는 -1로 주어진다.
# 기차 종류의 번호가 key이고 출발하는 시간들을 values로 갖는 dict에 정보 저장
# 같은 시간에 출발하는 기차는 없다고 가정.

# N번 역으로 이동했을 때, 가장 마지막에 탄 기차의 번호를 출력하는 프로그램 작성
# 기차들 속도가 다 같다고 가정하면
# 출발순서대로 역에 도착하니까 자기가 탄거 바로 다음 출발시간인 기차로 갈아탐

# import sys
#
# T, M, N = map(int, sys.stdin.readline().strip().split())
# # train_infos = {}
# train_infos = []
# for i in range(T):
#     infos = sys.stdin.readline().strip().split()
#     train_num = infos[0]
#     # train_time = []
#     for i in range(1, len(infos)):
#         if infos[i] != '-1':
#             train_infos.append([train_num, infos[i]])
#             # train_time.append(infos[i])
#     # train_infos[train_num] = train_time
# train_infos.sort(key=lambda x:x[1])
# # print(train_infos)
#
# first_train = int(train_infos[0][1])
# first_idx = 1
# for train_info in train_infos:
#     if int(train_info[1]) >= M:
#         first_train = int(train_info[1])
#         first_idx = train_infos.index(train_info) + 1
#         break
# # print(first_train)
# # print(first_idx)
# N -= first_idx + 1
# # print(N % len(train_infos))
# print(train_infos[(N % len(train_infos))-1][0])

import sys

# Read first line for basic info
info = input().split()
start_time = int(info[1])
destination = int(info[2])

# Process train schedules
trains = []
n = int(info[0])  # Number of trains
for _ in range(n):
    line = input().split()
    name = line[0]
    # Convert times to integers and exclude the last element
    times = list(map(int, line[1:-1]))

    # Create entries for each time with train name
    for time in times:
        trains.append([time, name])

# Sort trains by departure time
trains.sort(key=lambda x: x[0])

# Find starting index (first train after or at start_time)
start_index = 0
for i, (time, _) in enumerate(trains):
    if time >= start_time:
        start_index = i
        break

# Calculate final train
remainder = destination % len(trains)
final_index = (start_index + remainder + len(trains) - 1) % len(trains)
solution = trains[final_index][1]

print(solution)
