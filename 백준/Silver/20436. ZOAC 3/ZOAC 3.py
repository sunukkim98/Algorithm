from sys import stdin

start = list(map(str, input().split()))
word = input()


def solution(start, word):
    # 3*10 리스트
    keyboard = [
        list(map(str, 'qwertyuiop')),
        list(map(str, 'asdfghjkl0')),
        list(map(str, 'zxcvbnm000'))
    ]
    right = 'yuiophjklbnm'

    now_l = start[0]  # 현재 왼손의 자판
    now_l_coor = (0, 0)  # 현재 왼손의 위치
    now_r = start[1]  # 현재 오른손의 자판
    now_r_coor = (0, 0)  # 현재 오른손의 위치

    # 왼손, 오른손의 위치 초기값 설정
    for i in range(3):
        for j in range(10):
            if keyboard[i][j] == now_l: now_l_coor = (i, j)
            if keyboard[i][j] == now_r: now_r_coor = (i, j)

    time = 0

    for char in word:
        # 오른손 사용
        if char in right:
            for i in range(3):
                # b(ㅠ)만 한 칸 들어가있음
                if i == 2:
                    loop_st = 4
                else:
                    loop_st = 5

                for j in range(loop_st, 10):
                    if keyboard[i][j] == char:
                        dist = abs(now_r_coor[0] - i) + abs(now_r_coor[1] - j)
                        time += dist + 1
                        now_r_coor = (i, j)

        # 왼손 사용
        else:
            for i in range(3):
                # b(ㅠ)만 한 칸 들어가있음
                if i == 2:
                    loop_en = 4
                else:
                    loop_en = 5

                for j in range(loop_en):
                    if keyboard[i][j] == char:
                        dist = abs(now_l_coor[0] - i) + abs(now_l_coor[1] - j)
                        time += dist + 1
                        now_l_coor = (i, j)

    return time


print(solution(start, word))