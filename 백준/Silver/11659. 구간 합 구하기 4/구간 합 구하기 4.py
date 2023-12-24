import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
dp = [0] * (n+1)

for i in range(1, n+1):
  dp[i] = dp[i-1] + nums[i-1]

for k in range(m):
  i, j = map(int, input().split())
  answer = dp[j] - dp[i] + nums[i-1]
  print(answer)