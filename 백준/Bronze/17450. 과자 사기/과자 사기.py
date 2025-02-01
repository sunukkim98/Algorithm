import sys
input = sys.stdin.readline

# 3개의 줄로 이루어진 s. n, u의 가격과 무게가 띄어쓰기를 사이에 두고 주어진다.
prices = list()
weights = list()
for _ in range(3):
    price, weight = map(int, input().split())
    prices.append(price)
    weights.append(weight)
# print(prices, weights)

# 각 s, n, u의 가성비를 계산한다.
cost_effec = []
for i in range(3):
    total_cost = prices[i] * 10
    if total_cost >= 5000:
        total_cost -= 500
    effect = (weights[i] * 10) / total_cost
    cost_effec.append(effect)
# print(cost_effec)

# 가장 가성비가 높은 과자의 이름(S, N, U)을 출력한다.
# print(cost_effec.index(max(cost_effec)))
if cost_effec.index(max(cost_effec)) == 0:
    print('S')
elif cost_effec.index(max(cost_effec)) == 1:
    print('N')
elif cost_effec.index(max(cost_effec)) == 2:
    print('U')