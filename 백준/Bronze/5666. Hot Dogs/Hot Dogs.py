import sys
input = sys.stdin.readline

while True:
    try:
        h, p = map(int, input().split())
        res = str(round(h / p, 2))
        # print(res)
        # print(round(h / p, 2))
        temp = res.split('.')
        if len(temp[1]) < 2:
            temp[1] += '0'
            # print(temp[1])
        # print(temp)
        print(f"{temp[0]}.{temp[1]}")
    except EOFError:
        break
    except ValueError:
        break
