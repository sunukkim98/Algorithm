import sys
input = sys.stdin.readline

# 다음 풀 문제: 실버 3

while True:
    bit_str = input().strip()
    if bit_str == '#':
        break
    cnt_one = 0
    for bit in bit_str:
        if bit == '1':
            cnt_one += 1
    # print(cnt_one)
    # print(bit_str[-1])
    if bit_str[-1] == 'e':
        if cnt_one % 2 == 0:
            bit_str = bit_str.replace('e', '0')
        else:
            bit_str = bit_str.replace('e', '1')
    elif bit_str[-1] == 'o':
        if cnt_one % 2 == 0:
            bit_str = bit_str.replace('o', '1')
        else:
            bit_str = bit_str.replace('o', '0')

    print(bit_str)
