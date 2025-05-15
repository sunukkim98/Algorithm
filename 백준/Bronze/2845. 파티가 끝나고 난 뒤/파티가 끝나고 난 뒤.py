import sys
input = sys.stdin.readline

num_of_people, area = map(int, input().split())
total = num_of_people * area
article_info = list(map(int, input().split()))
for info in article_info:
    print(info - total, end=" ")
