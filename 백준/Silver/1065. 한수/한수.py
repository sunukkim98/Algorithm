import sys
input = sys.stdin.readline

# 다음 풀 문제: 실버 4

# 첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.
n = int(input().strip())
cnt = 0
for i in range(1, n+1):
    if len(str(i)) <= 2:
        cnt += 1
    elif len(str(i)) == 3:
        if int(str(i)[0]) - int(str(i)[1]) == int(str(i)[1]) - int(str(i)[2]):
            # print(str(i)[0], str(i)[1], str(i)[2])
            cnt += 1


print(cnt)
