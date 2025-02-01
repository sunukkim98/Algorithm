import sys
input = sys.stdin.readline
import math

def is_prime_num(n):
    # 2부터 n의 제곱근까지의 모든 수를 확인
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

og_num, add_code = input().split()
update_num = add_code + og_num
if is_prime_num(int(update_num)) and is_prime_num(int(og_num)):
    print('Yes')
else:
    print('No')