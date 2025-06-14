import sys
input = sys.stdin.readline

B, C, D = map(int, input().split())
min = min(B, C, D)
burgers = list(map(int, input().split()))
side_menus = list(map(int, input().split()))
drinks = list(map(int, input().split()))

burgers.sort(reverse=True)
side_menus.sort(reverse=True)
drinks.sort(reverse=True)

# print(burgers)
# print(side_menus)
# print(drinks)

og_price = 0
for i in range(len(burgers)):
    og_price += burgers[i]
for i in range(len(side_menus)):
    og_price += side_menus[i]
for i in range(len(drinks)):
    og_price += drinks[i]

price = 0
for i in range(min):
    price += round((burgers[i] + side_menus[i] + drinks[i]) * 0.9)

burgers = burgers[min:]
for i in range(len(burgers)):
    price += burgers[i]
side_menus = side_menus[min:]
for i in range(len(side_menus)):
    price += side_menus[i]
drinks = drinks[min:]
for i in range(len(drinks)):
    price += drinks[i]

print(og_price)
print(price)
