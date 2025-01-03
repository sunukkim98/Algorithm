# 테스트 케이스의 개수 t를 입력받는다.
# 정수나 소수인 숫자(0 <= num <= 100), 최대 3개의 연산자를 다음 줄에 입력받는다.
# 해당 숫자 이후의 연산에 대해 수행한다.
# @ = 3을 곱함
# % = 5를 더함
# #는 7을 뺌
# 입력된 연산이 ''인 경우 연산 수행을 종료

import sys

t = int(sys.stdin.readline().strip())
for i in range(t):
    inputs = sys.stdin.readline().strip().split()
    num = float(inputs[0])
    ops = inputs[1:]
    for op in ops:
        if op == '@':
            num *= 3
        if op == '%':
            num += 5
        if op == '#':
            num -= 7
    print(f'{num:.2f}')