import sys
input = sys.stdin.readline

# input:
A, B = input().split()
# print(A, B)

# A와 B에 모두 등장하는 첫 번째 단어, idx 저장
first_letter = ''
A_idx = -99
for i in range(len(A)):
    if A[i] in B:
        first_letter = A[i]
        A_idx = i
        break
for i in range(len(B)):
    if B[i] == first_letter:
        B_idx = i
        break
# print(first_letter, A_idx, B_idx)

out = []
for i in range(len(B)):
    out.append('')
    for j in range(len(A)):
        if i == B_idx:
            out[i] = A
        else:
            if j == A_idx:
                out[i] += B[i]
            else:
                out[i] += '.'
for i in range(len(out)):
    print(out[i])
