import sys
from collections import deque
input = sys.stdin.readline

m, n, h = map(int, input().split())

arr = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

que = deque()

def bfs():
  while que:
    z, x, y = que.popleft()

    for i in range(6):
      nx = x + dx[i]
      ny = y + dy[i]
      nz = z + dz[i]
      if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
        if arr[nz][nx][ny] == 0:
          arr[nz][nx][ny] = arr[z][x][y] + 1
          que.append((nz, nx, ny))
        

for i in range(h):
  for j in range(n):
    for k in range(m):
      if arr[i][j][k] == 1:
        que.append((i, j, k))

bfs()

temp = False
day = 0

for i in range(h):
  for j in range(n):
    for k in range(m):
      if arr[i][j][k] == 0:
        temp = True
      day = max(day, arr[i][j][k])

if temp:
  print(-1)
else:
  print(day - 1)