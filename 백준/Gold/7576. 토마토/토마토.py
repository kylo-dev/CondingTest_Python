from collections import deque

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(m)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

que = deque()
for i in range(m):
  for j in range(n):
    if arr[i][j] == 1:
      que.append((i, j))

def bfs():
  while que:
    a, b = que.popleft()
    for i in range(4):
      nx = a + dx[i]
      ny = b + dy[i]
      if -1 < nx < m and -1 < ny < n and arr[nx][ny] == 0:
        arr[nx][ny] = arr[a][b] + 1
        que.append((nx, ny))

bfs()

res = 0
for i in arr:
  for j in i:
    if j == 0:
      print(-1)
      exit(0)
  res = max(res, max(i))
print(res - 1)