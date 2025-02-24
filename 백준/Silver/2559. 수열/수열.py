
N, K = map(int, input().split())
nums = list(map(int, input().split()))

max_sum = sum(nums[:K])
win_sum = max_sum

for i in range(K, N):
  win_sum = win_sum - nums[i-K] + nums[i]
  max_sum = max(max_sum, win_sum)

print(max_sum)