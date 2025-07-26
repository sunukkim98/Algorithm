import sys
input = sys.stdin.readline

sum = 0
while True:
    betting_money = int(input().strip())
    if betting_money == -1:
        break
    sum += betting_money
print(sum)
