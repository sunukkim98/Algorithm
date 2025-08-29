import sys
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline
# import math

# 다음 풀 문제: 실버 4

# 1302번 베스트셀러

# 첫째 줄에 오늘 하루 동안 팔린 책의 개수 N이 주어진다.
n = int(input().strip())

books = {}

# 둘째부터 N개의 줄에 책의 제목이 입력으로 들어온다.
for _ in range(n):
    book = input().strip()
    if book not in books:
        books[book] = 1
    else:
        books[book] += 1

max_books = []
for key in books.keys():
    if books[key] == max(books.values()):
        max_books.append(key)

# print(books)
# print(max(books))
# print(max_books)
max_books.sort()
print(max_books[0])
