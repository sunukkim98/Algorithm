import sys
input = sys.stdin.readline

# 이용하여 순열을 구할수 있다
from itertools import permutations as p

# 첫째 줄에 X가 주어진다. (1 <= X <= 999,999)
X = input().strip()

# X와 구성이 같으면서 X보다 큰 수 중 가장 작은 수를 출력한다. 만약 그러한 숫자가 없는 경우에는 0을 출력한다.
permu = (sorted(set(map(lambda x: ''.join(x), p(X, len(X))))))
print(0) if permu[-1] == X else print(permu[permu.index(X) + 1])