import sys
input = sys.stdin.readline

correct_board = [input().strip() for _ in range(3)]
guess_board = [input().strip() for _ in range(3)]

correct_dict = {}
guess_dict = {}

for i in range(3):
    for j in range(3):
        if correct_board[i][j] in correct_dict:
            correct_dict[correct_board[i][j]] += 1
        else:
            correct_dict[correct_board[i][j]] = 1

        if guess_board[i][j] in guess_dict:
            guess_dict[guess_board[i][j]] += 1
        else:
            guess_dict[guess_board[i][j]] = 1

# print(correct_dict)
# print(guess_dict)

yellow_candidate = 0
for key in guess_dict.keys():
    if key in correct_dict:
        yellow_candidate += min(correct_dict[key], guess_dict[key])
# print(yellow_candidate)

green = 0
for i in range(3):
    for j in range(3):
        if correct_board[i][j] == guess_board[i][j]:
            green += 1

yellow = yellow_candidate - green

print(green)
print(yellow)
