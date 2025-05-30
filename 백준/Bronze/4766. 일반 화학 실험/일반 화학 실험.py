import sys
input = sys.stdin.readline

past_input = float(input().strip())
while True:
    current_input = float(input().strip())
    if current_input == 999:
        break
    print(f"{current_input - past_input:.2f}")
    past_input = current_input
