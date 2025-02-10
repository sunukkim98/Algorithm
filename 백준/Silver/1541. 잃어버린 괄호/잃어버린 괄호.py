import sys
input = sys.stdin.readline

'''
입력:
    첫째 줄에 식이 주어진다.
    식은 '0'~'9', '+'. '-'만으로 이루어져 있고, 가장 처음과 마지막 문자는 숫자이다.
    그리고 연속해서 두 개 이상의 연산자가 나타나지 않고, 5자리보다 많이 연속되는 숫자는 없다.
    수는 0으로 시작할 수 있다.
    입력으로 주어지는 식의 길이는 50보다 작거나 같다.
'''
equation = input().strip()
split_minus = equation.split('-')
added_nums = []
for subset in split_minus:
    result = 0
    temp = subset.split('+')
    for i in temp:
        result += int(i)
    added_nums.append(result)
final = added_nums[0]
for i in range(1, len(added_nums)):
    final -= added_nums[i]
print(final)

'''
출력:
    첫째 줄에 정답을 출력한다.
'''