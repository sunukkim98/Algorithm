# 첫째 줄에 저장된 사이트 주소의 수 N(1 <= N <= 100,000)과 찾으려는 주소의 수 M(1 <= M <= 100,000)을 입력받는다.
# N개의 줄에 걸쳐 각 줄에 사이트 주소와 비밀번호가 공백으로 구분해 입력받는다.
# M개의 줄에 걸쳐 비밀번호를 찾으려는 사이트 주소를 입력받는다.
# 사이트 주소에 대응되는 비밀번호를 출력한다.

import sys

n, m = map(int, sys.stdin.readline().strip().split())

passwd_dict = {}

for i in range(n):
    site, passwd = sys.stdin.readline().strip().split()
    passwd_dict[site] = passwd

for i in range(m):
    query = sys.stdin.readline().strip()
    print(passwd_dict[query])