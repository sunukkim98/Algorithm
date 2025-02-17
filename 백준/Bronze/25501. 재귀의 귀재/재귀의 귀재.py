import sys
input = sys.stdin.readline

import string

def recursion(s: string,
              l: int,
              r: int,
              cnt: int):
    if (l >= r):
        return 1, cnt
    elif (s[l] != s[r]):
        return 0, cnt
    else:
        return recursion(s, l+1, r-1, cnt + 1)

def isPalindrome(s: string):
    return recursion(s, 0, len(s) - 1, 1)

'''
문제:
    정휘는 위에 작성된 isPalindrome 함수를 이용하여 어떤 문자열이 팰린드롬인지 여부를 판단하려고 한다.
    구체적으로는, 문자열 S를 isPalindrome 함수의 인자로 전달하여 팰린드롬 여부를 반환값으로 알아낼 것이다.
    더불어 판별하는 과정에서 recursion 함수를 몇 번 호출하는지 셀 것이다.
    정휘를 따라 여러분도 함수의 반환값과 recursion 함수의 호출 횟수를 구해보자.
'''

'''
입력:
    첫째 줄에 테스트케이스의 개수 T가 주어진다. (1 <= T <= 1,000)
    둘째 줄부터 T개의 줄에 알파벳 대문자로 구성된 문자열 S가 주어진다.(1 <= |S| <= 1,000)
'''
T = int(input().strip())
for _ in range(T):
    ret_val, func_cnt = isPalindrome(input().strip())
    print(ret_val, func_cnt)

'''
출력:
    각 테스트케이스마다, isPalindrome 함수의 반환값과 recursion 함수의 호출 횟수를 한 줄에 공백으로 구분하여 출력한다.
'''