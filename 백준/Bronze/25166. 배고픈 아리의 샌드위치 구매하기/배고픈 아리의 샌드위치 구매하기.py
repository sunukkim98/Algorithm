import sys
input = sys.stdin.readline

'''
입력:
    샌드위치 가격 S(1 <= S <= 2048)와 쿠기가 가지고 있는 금액 M(1 <= M 1023)이 주어진다.
'''
S, M = map(int, input().split())

coins = [512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
coogie_coins = []

for coin in coins:
    if M >= coin:
        coogie_coins.append(coin)
        M -= coin
# print("coogie coin:", coogie_coins)

for coin in coins:
    if S >= coin:
        S -= coin
    # print("coin: ", coin, "\nrest price:", S)

if S == 0:
    print("No thanks")
else:
    for coin in coogie_coins:
        if S >= coin:
            S -= coin
    if S == 0:
        print("Thanks")
    else:
        print("Impossible")

'''
출력:
    아리의 돈으로만 살 수 있다면 "No thanks"를 출력
    쿠기의 도움을 받아야만 살 수 있다면 "Thanks"
    그리고 쿠기가 돈을 빌려주더라도 샌드위치를 살 수 없다면 "Impossible"를 출력
'''