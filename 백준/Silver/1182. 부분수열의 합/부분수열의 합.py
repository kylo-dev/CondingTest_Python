import sys
input = sys.stdin.readline

n, s = map(int, input().split())

arr = list(map(int, input().split()))
result = 0

def dfs(idx, sub_sum):
  global result

  if idx == n :
    return

  sub_sum += arr[idx]

  if sub_sum == s:
    result += 1

  dfs(idx + 1, sub_sum)
  dfs(idx + 1, sub_sum - arr[idx])

dfs(0, 0)
print(result)