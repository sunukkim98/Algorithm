# 두 정수 R1과 S를 입력받는다.(두 수의 범위: -1000 < 두 수 <= 1000)
# S에 2를 곱하고 R1을 뺀 결과를 출력한다.

r1, s = input().split()
r1 = int(r1)
s = int(s)

r2 = (s * 2) - r1
print(r2)