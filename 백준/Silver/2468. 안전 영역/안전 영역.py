import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
max_height = max(map(max, graph))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = []

def bfs(i, j, limit):
  que = deque([(i, j)])
  visited[i][j] = True
  
  while que:
    x, y = que.popleft()
    for k in range(4):
      nx = x + dx[k]
      ny = y + dy[k]
      if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
        if graph[nx][ny] > limit:
          visited[nx][ny] = True
          que.append((nx, ny))
        else:
          visited[nx][ny] = True

for limit in range(max_height + 1):
  visited = [[False] * N for _ in range(N)]
  cnt = 0

  for i in range(N):
    for j in range(N):
      if not visited[i][j]:
        if graph[i][j] <= limit:
          visited[i][j] = True
        else:
          bfs(i, j, limit)
          cnt += 1
  result.append(cnt)

if not len(result):
  print(0)
else:
  print(max(result))