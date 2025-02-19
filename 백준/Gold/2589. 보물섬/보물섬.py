import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
  visited = [[0] * M for _ in range(N)]
  que = deque([(i, j)])
  visited[i][j] = 1
  result = 0

  while que:
    x, y = que.popleft()

    for k in range(4):
      nx = x + dx[k]
      ny = y + dy[k]

      if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 'L':
        if visited[nx][ny] == 0:
          que.append((nx, ny))
          visited[nx][ny] = visited[x][y] + 1
          result = max(result, visited[nx][ny])
  return result - 1

result = 0
for i in range(N):
  for j in range(M):
    if graph[i][j] == "L":
      cnt = bfs(i, j)
      result = max(result, cnt)

print(result)
