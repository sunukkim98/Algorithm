import sys
input = sys.stdin.readline

'''
입력:
    첫번째 줄에는 사람들이 만난 기록의 수 N (1 <= N <= 1,000)이 주어진다.
    두번째 줄부터 N개의 줄에 걸쳐 사람들이 만난 기록이 주어진다.
    i + 1번째 줄에는 i번째로 만난 사람들의 이름 A_i와 B_i가 공백을 사이에 두고 주어진다.
'''
N = int(input().strip())
first_dancer = 'ChongChong'
dancing_peoples = set()
for i in range(N):
    lines = input().strip().split()
    if first_dancer in lines or lines[0] in dancing_peoples or lines[1] in dancing_peoples:
        dancing_peoples.add(lines[0])
        dancing_peoples.add(lines[1])
        
'''
출력:
    마지막 기록 이후 무지개 댄스를 추는 사람의 수를 출력하라.
'''
print(len(dancing_peoples))