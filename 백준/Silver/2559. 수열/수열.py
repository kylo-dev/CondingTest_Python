N, K = map(int, input().split())
arr = list(map(int, input().split()))

win_sum = sum(arr[:K])
max_sum = win_sum

for i in range(K, N):
  win_sum = win_sum + arr[i] - arr[i-K]
  max_sum = max(max_sum, win_sum)

print(max_sum)