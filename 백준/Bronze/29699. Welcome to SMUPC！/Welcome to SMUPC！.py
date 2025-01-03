import sys

label = 'WelcomeToSMUPC'
# print(len(label))
N = int(sys.stdin.readline().strip())
N %= 14
print(label[N - 1])