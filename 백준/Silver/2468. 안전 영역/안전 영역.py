import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

answer = []

max_n = 0

for i in arr:
  max_n = max(max_n, max(i))
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, limit):
  que = deque([(x, y)])
  visited[x][y] = True

  while que:
    x, y = que.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < n:
        if not visited[nx][ny]:
          if arr[nx][ny] > limit:
            visited[nx][ny] = True
            que.append((nx, ny))
          else:
            visited[nx][ny] = True

for i in range(max_n + 1):
  visited = [[False for _ in range(n)] for _ in range(n)]
  cnt = 0
  for x in range(n):
    for y in range(n):
      if not visited[x][y]:
        if arr[x][y] <= i:
          visited[x][y] = True
        else:
          bfs(x, y, i)
          cnt += 1
  answer.append(cnt)

if len(answer) == 0:
  print(0)
else:
  print(max(answer))