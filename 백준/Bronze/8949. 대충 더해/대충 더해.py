import sys
input = sys.stdin.readline

A, B = input().split()

if len(A) > len(B):
    # print(len(A) - len(B))
    base = B
    remain = A[:len(A) - len(B)]
else:
    # print(len(B) - len(A))
    base = A
    remain = B[:len(B) - len(A)]
# print(remain)

res = ""
for i in reversed(range(1, len(base) + 1)):
    # print(A[-i], B[-i])
    res += f"{int(A[-i]) + int(B[-i])}"

print(f"{remain}{res}")
# for i in reversed(range(len(res))):
#     remain += res[i]
# print(remain)
