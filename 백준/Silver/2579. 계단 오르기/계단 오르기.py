import sys
input = sys.stdin.readline

t = int(input())

dp = [0] * (t + 1)
stair = [int(input()) for _ in range(t)]

for i in range(1, t+1):

  if i == 1:
    dp[i] = stair[i-1] # stair[0] : 1층
  elif i == 2:
    dp[i] = stair[i-2] + stair[i-1]
  elif i == 3:
    dp[i] = max((stair[i-2]+stair[i-1]), (stair[i-3] + stair[i-1]))
  else:
    dp[i] = max((stair[i-1] + stair[i-2] + dp[i-3]), (stair[i-1] + dp[i-2]))

print(dp[t])