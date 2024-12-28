# 정수를 입력받는다. 정수의 범위(1~10^9)
# 정수가 7을 포함하는지 확인한다.
# 정수가 7로 나누어 나머지가 0인지 확인한다.
# 확인된 정보를 통해 다음 조건에 따라 0~3값을 출력한다.
# Print 0 if the number does not contain 7 and is not divisible by 7.
# Print 1 if the number does not contain 7 but is divisible by 7.
# Print 2 if the number does contain 7 but is not divisible by 7.
# Print 3 if the number does contain 7 and is divisible by 7.

n = input()
int_n = int(n)

flag1 = False
if n.find('7') != -1:
    flag1 = True

flag2 = False
if int_n % 7 == 0:
    flag2 = True

if not flag1 and not flag2:
    print(0)
elif not flag1 and flag2:
    print(1)
elif flag1 and not flag2:
    print(2)
elif flag1 and flag2:
    print(3)