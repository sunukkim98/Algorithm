import sys
input = sys.stdin.readline

# 버거의 가격을 입력받는다.
burger_prices = []
for i in range(3):
    burger_prices.append(int(input().strip()))

# 음료의 가격을 입력받는다.
drink_prices = []
for i in range(2):
    drink_prices.append(int(input().strip()))

# 각 버거와 음료의 가격을 더한 가격들 중 최소값을 구한다
burger_prices.sort()
drink_prices.sort()
min_price = burger_prices[0] + drink_prices[0]

# 최소 가격에서 50원을 뺀 가격을 출력한다
print(min_price - 50)