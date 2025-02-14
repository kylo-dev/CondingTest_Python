import sys
input = sys.stdin.readline
from collections import deque


N, L, R = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j, visited):
  que = deque([(i, j)])
  visited[i][j] = True
  total = graph[i][j]
  union = [(i, j)]

  while que:
    x, y = que.popleft()
    
    for k in range(4):
      nx = x + dx[k]
      ny = y + dy[k]

      if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
        if L <= abs(graph[x][y] - graph[nx][ny]) <= R:
          total += graph[nx][ny]
          visited[nx][ny] = True
          que.append((nx, ny))
          union.append((nx, ny))
        
  
  if len(union) == 1:
    return False
  
  new_population = total // len(union)
  for x, y in union:
    graph[x][y] = new_population
  return True


result = 0
while True:

  visited = [[False] * N for _ in range(N)]
  moved = False

  for i in range(N):
    for j in range(N):
      if not visited[i][j]:
        if bfs(i, j, visited):
          moved = True
  
  if moved:
    result += 1
  else:
    break

print(result)