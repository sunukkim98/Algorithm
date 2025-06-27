import sys
input = sys.stdin.readline

char_list = "abcdefghijklmnopqrstuvwxyz"

t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    a = list(map(int, input().split()))
    # print(a)
    for j in a:
        print(char_list[j], end='')
        current_char = char_list[j]
        temp = char_list.replace(current_char, '')
        char_list = current_char + temp
    char_list = "abcdefghijklmnopqrstuvwxyz"
    print()
