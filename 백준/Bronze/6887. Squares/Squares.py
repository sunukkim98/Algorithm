import sys
input = sys.stdin.readline

num_of_tiles = int(input())

num = 1
while True:
    if num * num > num_of_tiles:
        print(f'The largest square has side length {num - 1}.')
        exit()
    num += 1