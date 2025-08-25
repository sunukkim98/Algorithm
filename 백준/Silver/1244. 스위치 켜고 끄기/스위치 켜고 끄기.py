import sys
input = sys.stdin.readline

# 다음 풀 문제: 실버 4

# 첫째 줄에는 스위치 개수가 주어진다. 스위치 개수는 100 이하인 양의 정수이다.
n_switch = int(input().strip())

# 둘째 줄에는 각 스위치의 상태가 주어진다. 켜져 있으면 1, 꺼져있으면 0이라고 표시하고 사이에 빈칸이 하나씩 있다.
switch_state = list(map(int, input().split()))

# 셋째 줄에는 학생수가 주어진다. 학생수는 100 이하인 양의 정수이다.
n = int(input().strip())

# print(switch_state)

# 넷째 줄부터 마지막 줄까지 한 줄에 한 학생의 성별, 학생이 받은 수가 주어진다. 남학생은 1로, 여학생은 2로 표시하고,
# 학생이 받은 수는 스위치 개수 이하인 양의 정수이다.
for _ in range(n):
    gender, num = map(int, input().split())
    if gender == 1:
        for i in range(1, n_switch + 1):
            if i % num == 0:
                if switch_state[i-1] == 0:
                    switch_state[i-1] = 1
                elif switch_state[i-1] == 1:
                    switch_state[i-1] = 0
    else:
        # print(num)
        if switch_state[num-1] == 0:
            switch_state[num-1] = 1
        elif switch_state[num-1] == 1:
            switch_state[num-1] = 0
        for i in range(1, (n_switch // 2) + 1):
            if (num-1 - i) >= 0 and (num-1 + i) < n_switch:
                if switch_state[num-1-i] == switch_state[num-1+i]:
                    if switch_state[num-1-i] == 0:
                        switch_state[num-1-i] = 1
                        switch_state[num-1+i] = 1
                    elif switch_state[num-1-i] == 1:
                        switch_state[num-1-i] = 0
                        switch_state[num-1+i] = 0
                else:
                    break
            else:
                break

    # print(switch_state)
# 스위치의 상태를 1번 스위치에서 시작하여 마지막 스위치까지 한 줄에 20개씩 출력한다.
for i in range(1, n_switch+1):
    if (i) % 20 == 0:
        print(switch_state[i-1], end='\n')
    else:
        print(switch_state[i-1], end=' ')
# print(' '.join(map(str, switch_state)))

