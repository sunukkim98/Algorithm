import sys
input = sys.stdin.readline

from collections import defaultdict

'''
문제:
    만들고자 하는 단어장의 단어 순서는 다음과 같은 우선순위를 차례로 적용하여 만들어진다.
    1. 자주 나오는 단어일수록 앞에 배치한다.
    2. 해당 단어의 길이가 길수록 앞에 배치한다.
    3. 알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치한다.
'''

'''
입력:
    첫째 줄에는 영어 지문에 나오는 단어의 개수 N과 외울 단어의 길이 기준이 되는 M이 공백으로 주어진다. (1 <= N <= 100,000, 1 <= M <= 10)
    둘째 줄부터 N+1번째 줄까지 외울 단어를 입력받는다.
    알파벳 소문자로만 주어진다.
'''
words_dict = defaultdict(int)
N, M = map(int, input().strip().split())
for _ in range(N):
    word = input().strip()
    if len(word) >= M:
        words_dict[word] += 1

words_dict = sorted(words_dict.items(), key = lambda x : (-x[1], -len(x[0]), x[0])) # x[0] = 단어, x[1] = 단어 빈도수

'''
출력:
    단어장에 들어 있는 단어를 단어장의 앞에 위치한 단어부터 한 줄에 한 단어씩 순서대로 출력한다.
'''
for i in words_dict:
    print(i[0])