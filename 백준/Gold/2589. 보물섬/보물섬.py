import sys
from collections import deque
input = sys.stdin.readline
import copy

L, W = map(int, input().split())

graph = [list(input().rstrip()) for _ in range(L)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0

def bfs(i, j):
  que = deque([(i, j)])
  visited[i][j] = 1

  while que:
    x, y = que.popleft()
    for k in range(4):
      nx = x + dx[k]
      ny = y + dy[k]
      if 0 <= nx < L and 0 <= ny < W and graph[nx][ny] == 'L' and not visited[nx][ny]:
        que.append((nx, ny))
        visited[nx][ny] = visited[x][y] + 1
  
  return visited

result = 0
for i in range(L):
  for j in range(W):
    if graph[i][j] == 'L':
      visited = [[0] * W for _ in range(L)]
      sub_res = bfs(i, j)
      result = max(result, max(max(s) for s in sub_res))


print(result - 1)