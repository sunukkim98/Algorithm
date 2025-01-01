# 가장 길게 낼 수 있는 문자열을 입력받는다.
# 의사가 듣기 원하는 듣기를 원하는 문자열을 입력받는다.
# 가장 길게 낼 수 있는 문자열의 길이가 의사가 듣기 원하는 문자열의 길이보다 적다면 no를 크거나 같다면 go출력

possible_ah = input()

input_ah = input()

if len(possible_ah) < len(input_ah):
    print('no')
else:
    print('go')