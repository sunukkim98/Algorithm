import sys
input = sys.stdin.readline

N = int(input().strip())

prices = []
for i in range(N):
    line = list(map(int, input().split()))
    num_cnt = [0 for _ in range(6)]
    for j in range(len(line)):
        if line[j] == 1:
            num_cnt[0] += 1
        if line[j] == 2:
            num_cnt[1] += 1
        if line[j] == 3:
            num_cnt[2] += 1
        if line[j] == 4:
            num_cnt[3] += 1
        if line[j] == 5:
            num_cnt[4] += 1
        if line[j] == 6:
            num_cnt[5] += 1

    price = 0
    cnt_two = 0
    for j in range(len(num_cnt)):
        if num_cnt[j] == 4:
            price = 50000 + ((j + 1) * 5000)
        if num_cnt[j] == 3:
            price = 10000 + ((j + 1) * 1000)
        if num_cnt[j] == 2:
            cnt_two += 1

    if cnt_two == 2:
        price = 2000
        for k in range(len(num_cnt)):
            if num_cnt[k] == 2:
                price += (k + 1) * 500

    if cnt_two == 1:
        price = 1000
        for k in range(len(num_cnt)):
            if num_cnt[k] == 2:
                price += (k + 1) * 100

    if price == 0:
        price = max(line) * 100

    prices.append(price)
print(max(prices))