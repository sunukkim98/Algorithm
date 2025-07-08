import sys
input = sys.stdin.readline

weight = float(input().strip())
height = float(input().strip())
bmi = weight / (height * height)
# print(bmi)
if bmi > 25:
    print("Overweight")
elif bmi > 18.5 and bmi < 25.0:
    print("Normal weight")
else:
    print("Underweight")