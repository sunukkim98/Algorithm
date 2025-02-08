import sys
input = sys.stdin.readline

'''
입력:
    첫 번째 줄에는 채팅방의 기록 수를 나타내는 정수 N이 주어진다. (1 <= N <= 100,000)
    두 번째 줄부터 N개의 줄에 걸쳐 새로운 사람의 입장을 나타내는 ENTER, 혹은 채팅을 
    입력한 유저의 닉네임이 문자열로 주어진다. (1 <= 문자열 길이 <= 20)
    첫 번째 주어지는 문자열은 무조건 ENTER이다.
'''
N = int(input().strip())
count_set = set()
count = 0
for _ in range(N):
    str = input().replace('\n', '')
    if str == 'ENTER':
        count_set = count_set - count_set
        continue
    if str in count_set:
        continue
    else:
        count_set.add(str)
        count += 1
print(count)