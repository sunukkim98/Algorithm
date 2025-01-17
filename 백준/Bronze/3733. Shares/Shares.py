import sys

while True:
    try:
        a,b = map(int,sys.stdin.readline().strip().split())
        print(b//(a+1))
    except:
        break