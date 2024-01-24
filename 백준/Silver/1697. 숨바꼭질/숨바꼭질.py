from collections import deque

n, k = map(int, input().split())

max = 100001
arr = [0] * max

def bfs(v):
  que = deque([v])

  while que:
    x = que.popleft()

    if x == k:
      print(arr[x])
      return

    for i in (x-1, x+1, x*2):
      if 0 <= i < max and (not arr[i]):
        arr[i] = arr[x] + 1
        que.append(i)

bfs(n)