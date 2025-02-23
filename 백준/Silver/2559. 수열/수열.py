import sys
input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(map(int, input().split()))

win_sum = sum(nums[:K])
max_sum = win_sum

for i in range(K, N):
  win_sum += nums[i] - nums[i-K]
  max_sum = max(max_sum, win_sum)

print(max_sum)