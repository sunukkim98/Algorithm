import sys

num_of_people = int(sys.stdin.buffer.readline().rstrip())
distance = int(sys.stdin.buffer.readline().rstrip())

print((num_of_people - 1) * distance)
