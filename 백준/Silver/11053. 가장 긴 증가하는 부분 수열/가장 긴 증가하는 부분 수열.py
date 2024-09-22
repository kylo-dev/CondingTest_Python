N = int(input())
arr = list(map(int, input().split()))

dp = [1] * 1001

for i in range(1, N):
  for j in range(0, i):
    if arr[i] > arr[j]:
      dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))