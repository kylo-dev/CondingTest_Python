from collections import deque
m, n, k = map(int, input().split())

arr = [[0] * n for _ in range(m)]

for i in range(k):
  x1, y1, x2, y2 = map(int, input().split())
  for j in range(y1, y2):
    for k in range(x1, x2):
      arr[j][k] = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
  que = deque([(x, y)])
  arr[x][y] = 1
  size = 1
  while que:
    x, y = que.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < m and 0 <= ny < n and arr[nx][ny] == 0:
        arr[nx][ny] = 1
        que.append((nx, ny))
        size += 1
  return size


result = []
for i in range(m):
  for j in range(n):
      if arr[i][j] == 0:
        result.append(bfs(i, j))

print(len(result))
print(' '.join(map(str, sorted(result))))