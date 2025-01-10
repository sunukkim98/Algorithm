# 임의의 자연수를 입력받는다.
# 1 2 3 4 5 4 3 2
# 1 2 3 4 5 4 3 2
# 1 2 3 4 5 4 3 2
# 1 2 3 4 5 4 3 2
# 1 2 3 4 5 4 3 2
# 1
# 1 2 3 4 5 4 3 2
# 1 2 3 4 5 4 3 2
# 1 2 3 4 5 4 3 2

import sys

finger_num = [1,2,3,4,5,4,3,2]
n = int(sys.stdin.readline().strip())
n = n%8
if n ==1 : print(1)
elif n in [2,0] : print(2)
elif n in [3,7] : print(3)
elif n in [4,6] : print(4)
elif n == 5 : print(5)