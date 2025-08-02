import sys
input = sys.stdin.readline

numbers = []
zero = "0000\n0  0\n0  0\n0  0\n0000"
one = "   1\n   1\n   1\n   1\n   1"
two = "2222\n   2\n2222\n2\n2222"
three = "3333\n   3\n3333\n   3\n3333"
four = "4  4\n4  4\n4444\n   4\n   4"
five = "5555\n5\n5555\n   5\n5555"
six = "6666\n6\n6666\n6  6\n6666"
seven = "7777\n   7\n   7\n   7\n   7"
eight = "8888\n8  8\n8888\n8  8\n8888"
nine = "9999\n9  9\n9999\n   9\n   9"

numbers.append(zero)
numbers.append(one)
numbers.append(two)
numbers.append(three)
numbers.append(four)
numbers.append(five)
numbers.append(six)
numbers.append(seven)
numbers.append(eight)
numbers.append(nine)

line = input().strip()
for i in range(len(line)):
    print(numbers[int(line[i])])
    # if i != len(line) - 1:
    print()
