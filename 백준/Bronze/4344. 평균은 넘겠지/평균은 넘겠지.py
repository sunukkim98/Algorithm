import sys
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline
# import math

# 다음 풀 문제: 브론즈 1

# 4344번 평균은 넘겠지

# 첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
c = int(input().strip())

# 둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 이어서 N명의 점수가 주어진다.
# 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.
for _ in range(c):
    line = list(map(int, input().split()))
    n = line[0]
    scores = line[1:]
    avg = sum(scores) / n
    # print(avg)
    cnt = 0
    for score in scores:
        if score > avg:
            cnt += 1

    # 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.
    # 정답과 출력값의 절대/상대 오차는 10-3이하이면 정답이다.
    print("{:.3f}%".format(round((cnt / n) * 100, 3)))
