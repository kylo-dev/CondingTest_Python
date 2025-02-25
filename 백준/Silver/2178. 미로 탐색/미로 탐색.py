import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
graph = []
for _ in range(N):
  graph.append(list(input().rstrip()))

for i in range(N):
  for j in range(M):
    graph[i][j] = int(graph[i][j])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False] * M for _ in range(N)]

def bfs(i, j):
  que = deque([(i, j)])
  visited[i][j] = True

  while que:
    x, y = que.popleft()

    for k in range(4):
      nx = x + dx[k]
      ny = y + dy[k]
      if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
        if graph[nx][ny] == 1:
          que.append((nx, ny))
          graph[nx][ny] = graph[x][y] + 1
          visited[x][y] = True
  return graph[-1][-1]

print(bfs(0, 0))