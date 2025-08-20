import sys
input = sys.stdin.readline

# 다음 풀 문제: 실버 4

# 첫째 줄에 N과 M이 주어진다.
n, m = map(int, input().split())

package_prices = []
six_prices = []
one_prices = []

# 둘째 줄부터 M개의 줄에는 각 브랜드의 패키지 가격과 낱개의 가격이 공백으로 구분하여 주어진다.
for _ in range(m):
    package_p, one_p = map(int, input().split())
    package_prices.append(package_p)
    six_prices.append(package_p)
    six_prices.append(one_p * 6)
    one_prices.append(one_p)

package_prices.sort()
six_prices.sort()
one_prices.sort()
# print(package_prices, six_prices, one_prices)

total = 0
total += (n // 6) * six_prices[0]
if n % 6 != 0:
    total += min(package_prices[0], (n % 6) * one_prices[0])
print(total)
