import sys
input = sys.stdin.readline

pic = [input().split() for _ in range(15)]
# print(pic)
for i in range(15):
    for j in range(15):
        if pic[i][j] == "w":
            print("chunbae")
            exit()
        elif pic[i][j] == "b":
            print("nabi")
            exit()
        elif pic[i][j] == "g":
            print("yeongcheol")
            exit()