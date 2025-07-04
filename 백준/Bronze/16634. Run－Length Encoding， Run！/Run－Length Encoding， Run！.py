import sys
input = sys.stdin.readline

command, message = input().split()
# print(command)
# print(message)
if command == 'E':
    # print('encode!')
    letter = ''
    cnt = 0
    for single_char in message:
        # print(single_char)
        if letter == '':
            letter = single_char
            cnt = 1
        elif letter == single_char:
            cnt += 1
        else:
            print(f"{letter}{cnt}", end='')
            letter = single_char
            cnt = 1
    print(f"{letter}{cnt}")
elif command == 'D':
    # print('decode!')
    letter = ''
    cnt = 0
    for single_char in message:
        if letter == '':
            letter = single_char
        else:
            cnt = int(single_char)
            for i in range(cnt):
                print(letter, end='')
            letter = ''
