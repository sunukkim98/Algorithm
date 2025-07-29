import sys
input = sys.stdin.readline

limit = int(input().strip())
speed = int(input().strip())

if speed <= limit:
    print("Congratulations, you are within the speed limit!")
else:
    gap = speed - limit
    if gap >= 1 and gap <= 20:
        fine = 100
    elif gap > 20 and gap <= 30:
        fine = 270
    else:
        fine = 500
    print(f"You are speeding and your fine is ${fine}.")
