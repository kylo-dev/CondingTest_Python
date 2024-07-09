from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
max_sum = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
  que = deque([(x, y)])
  arr[x][y] = 0
  max_cnt = 1
  while que:
    x, y = que.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1:
        que.append((nx, ny))
        arr[nx][ny] = 0
        max_cnt += 1
  return max_cnt

for i in range(n):
  for j in range(m):
    if arr[i][j] == 1:
      cnt += 1
      max_sum = max(max_sum, bfs(i, j))

print(cnt)
print(max_sum)