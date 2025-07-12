import sys
input = sys.stdin.readline

for _ in range(3):
    s_h, s_m, s_s, e_h, e_m, e_s = map(int, input().split())
    start_sec = (s_h * 60 * 60) + (s_m * 60) + (s_s)
    end_sec = (e_h * 60 * 60) + (e_m * 60) + (e_s)
    working_sec = end_sec - start_sec
    w_s = working_sec % 60
    w_m = working_sec // 60
    w_h = w_m // 60
    w_m %= 60
    print(w_h, w_m, w_s)