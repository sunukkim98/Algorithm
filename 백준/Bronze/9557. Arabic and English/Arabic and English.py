import sys
input = sys.stdin.readline

n = int(input().strip())
for _ in range(n):
    word_len = int(input().strip())
    words = input().split()
    # print(words)

    arabian = []
    alphabet = []
    flag = False
    for word in words:
        if word.isalpha():
            flag = True
        if not flag:
            arabian.append(word)
        else:
            alphabet.append(word)
    # print(arabian)
    # print(alphabet)

    res = ""
    if len(alphabet) == 0:
        for i in range(len(arabian)):
            res += arabian[i]
            if i != len(arabian) - 1:
                res += " "
    else:
        alphabet.append(alphabet[0])
        del alphabet[0]
        # print(arabian)
        # print(alphabet)
        for i in range(len(alphabet)):
            res += alphabet[i]
            res += " "
        for i in range(len(arabian)):
            res += arabian[i]
            if i != len(arabian) - 1:
                res += " "
    print(res)
