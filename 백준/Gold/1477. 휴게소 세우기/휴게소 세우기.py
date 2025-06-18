import sys, math

input = sys.stdin.readline

N, M, L = map(int, input().split())
arr = [0] + sorted(map(int, input().split())) + [L]

left, right = 1, L
answer = right

while left <= right:
  mid = (left + right) // 2
  count = 0

  for i in range(1, len(arr)):
    diff = arr[i] - arr[i-1]

    if diff > mid:
      count += math.ceil(diff / mid) - 1

    if count > M:
      left = mid + 1
      break

  if count <= M:
    answer = min(answer, mid)
    right = mid - 1

print(answer)
