import sys
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    left_word, right_word = input().split()
    left_word_list = list(left_word)
    right_word_list = list(right_word)
    left_word_list.sort()
    right_word_list.sort()
    # print(left_word_list)
    # print(right_word_list)
    if left_word_list == right_word_list:
        print(f"{left_word} & {right_word} are anagrams.")
    else:
        print(f"{left_word} & {right_word} are NOT anagrams.")
