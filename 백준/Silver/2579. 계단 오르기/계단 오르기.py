import sys

# 입력의 첫째 줄에 계단의 개수가 주어진다.
num_of_stairs = int(sys.stdin.readline().strip())

# 각 계단의 수만큼 반복:
#     한 줄에 하나씩 제일 아래에 놓인 계단부터 순서대로 각 계단에 쓰여 있는 점수가 주어진다.
stair_weights = [0] * (num_of_stairs + 1)
for i in range(1, num_of_stairs + 1):
    weight = int(sys.stdin.readline().strip())
    stair_weights[i] = weight
# print(stair_weights)

if num_of_stairs == 1:
    print(stair_weights[1])
    exit()
elif num_of_stairs == 2:
    print(sum(stair_weights[:3]))
    exit()

# 점화식: dp[i] = max(
#     dp[i-3] + stair_weights[i-1] + stair_weights[i],
#     dp[i-2] + stair_weights[i]
# )
dp = [0] * (num_of_stairs + 1)
dp[1] = stair_weights[1]
dp[2] = stair_weights[1] + stair_weights[2]
for i in range(3, num_of_stairs + 1):
    dp[i] = max(
        dp[i-3] + stair_weights[i-1] + stair_weights[i],
        dp[i-2] + stair_weights[i]
    )
print(dp[num_of_stairs])