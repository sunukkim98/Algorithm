# add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
# remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
# check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
# toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
# all: S를 {1, 2, ..., 20} 으로 바꾼다.

import sys

def check_list(set, q_n):
    if q_n in set:
        return 1
    else:
        return 0

def add(set, q_n):
    if check_list(set, q_n):
        return set
    else:
        set.append(q_n)
        return set

def remove(set, q_n):
    if check_list(set, q_n):
        del set[set.index(q_n)]
        return set
    else:
        return set

def toggle(set, q_n):
    if check_list(set, q_n):
        del set[set.index(q_n)]
        return set
    else:
        set.append(q_n)
        return set

def empty(set):
    set.clear()
    return set

def all(set):
    set.clear()
    for i in range(1,21):
        set.append(i)
    return set

M = int(sys.stdin.readline().strip())
S = []
for i in range(M):
    query = sys.stdin.readline().strip()
    if query.find('add') > -1:
        op, q_n = query.split()
        q_n = int(q_n)
        S = add(S, q_n)
    elif query.find('remove') > -1:
        op, q_n = query.split()
        q_n = int(q_n)
        S = remove(S, q_n)
    elif query.find('check') > -1:
        op, q_n = query.split()
        q_n = int(q_n)
        print(check_list(S, q_n))
    elif query.find('toggle') > -1:
        op, q_n = query.split()
        q_n = int(q_n)
        S = toggle(S, q_n)
    elif query.find('all') > -1:
        S = all(S)
    elif query.find('empty') > -1:
        S = empty(S)
    # print(S)