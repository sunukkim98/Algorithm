# 첫째 줄에 테스트 케이스의 개수 T를 입력받는다.
# 테스트 케이스의 개수 T만큼 반복:
#     정수 n을 입력받는다.(0 < n < 11)
#     n을 1, 2, 3의 합으로 나타내는 방법의 수를 구해 출력한다.

import sys

def get_num_of_ways(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    return get_num_of_ways(n-1)+get_num_of_ways(n-2)+get_num_of_ways(n-3)

T = int(sys.stdin.readline().strip())
for i in range(T):
    n = int(sys.stdin.readline().strip()) # (0 < n < 11)
    print(get_num_of_ways(n))

