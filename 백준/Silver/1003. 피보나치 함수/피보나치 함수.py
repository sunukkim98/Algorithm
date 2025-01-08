# 피보나치 수를 구하는 함수에서 n==0인 경우와 n==1인 경우를 더해 출력한다

import sys

def fibonacci(n):
    zeros = [0 for i in range(n+2)]
    ones = [0 for i in range(n+2)]
    zeros[0] = 1
    zeros[1] = 0
    ones[0] = 0
    ones[1] = 1

    for i in range(2,n+1):
        zeros[i] = zeros[i-1] + zeros[i-2]
        ones[i] = ones[i-1] + ones[i-2]

    return zeros[n], ones[n]

t = int(sys.stdin.readline().strip())
for i in range(t):
    num = int(sys.stdin.readline().strip())
    # print(fibonacci(num))
    zero, one = fibonacci(num)
    print(zero, one)