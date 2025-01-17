# 후보의 수를 입력받는다.
# 후보의 수만큼 반복한다:
#     입력받은 숫자가 5이상이면 5를 빼고 결과에 '+++++ '를 추가한다.
#     5미만이면 결과에 남은 숫자 * '|'를 추가한다.
#     숫자가 0이 되면 다음 후보에 대해서 실행

import sys

candidate_num = int(sys.stdin.readline().strip())
for _ in range(candidate_num):
    n = int(sys.stdin.readline().strip())
    result = ''
    while n != 0:
        if n >= 5:
            result = f'{result}++++ '
            n -= 5
        else:
            result = f'{result}|'
            n -= 1
    print(result)