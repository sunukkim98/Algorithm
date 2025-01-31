import sys
input = sys.stdin.readline

# 수열의 크기 n이 주어진다.
n = int(input())

# 수열에 포함되는 수를 한 줄에 입력받아 리스트에 저장한다.
sequence = list(map(int, input().strip().split()))

# x를 입력받는다.
x = int(input())

# 수열을 오름차순 정렬한다.
sequence.sort()

# 수열 원소가 x에서 해당 수열 원소를 뺀 값보다 작다면 나머지 원소에 뺀 값이 있는지 찾아 있으면 경우의 수 증가
# cnt = 0
# for i in range(len(sequence)):
#     if sequence[i] < (x - sequence[i]):
#         try:
#             sequence.index(x - sequence[i])
#             cnt += 1
#         except:
#             continue
cnt = 0
start = 0
end = n-1

while start < end:
    s = sequence[start] + sequence[end]

    if s == x:
        cnt += 1
        start += 1
    elif s > x:
        end -= 1
    else:
        start += 1

print(cnt)