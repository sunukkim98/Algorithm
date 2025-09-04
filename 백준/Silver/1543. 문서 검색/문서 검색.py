import sys
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline
# import math

# 다음 풀 문제: 실버 5

# 1543번 문서 검색

docs = input().replace('\n', '')
# print(docs)

word = input().replace('\n', '')

# cnt = 0
#
# # while True:
# #     if len(word) > len(docs):
# #         break
# #     if len(word) == len(docs):
# #         if word == docs:
# #             cnt += 1
# #         break
# #     for i in range(len(docs)):
# #         if len(docs[i:len(word) + i]) == len(word):
# #             if docs[i:len(word) + i] == word:
# #                 cnt += 1
# #                 docs = docs[len(word) + i:]
# #                 # print(docs)
# #                 break
# #         else:
# #             break
#
# for i in range(len(docs)):
#     print(docs)
#     if len(docs[i:len(word) + i]) == len(word):
#         if docs[i:len(word) + i] == word:
#             cnt += 1
#             docs = docs[len(word) + i:]
#             print(docs)
#     else:
#         break
# print(cnt)

sp_docs = docs.split(word)
print(len(sp_docs) - 1)
