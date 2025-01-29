from collections import deque
import sys
input = sys.stdin.readline

# 남북서동 상하
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

while True:
  L, R, C = map(int, input().split())
  
  if L == 0 and R == 0 and C == 0:
    break

  start = None
  board = []
  visited = [[[False] * C for _ in range(R)] for _ in range(L)]

  for i in range(L):
    board.append([list(input().strip()) for _ in range(R)])
    input()

    for x in range(R):
      for y in range(C):
        if board[i][x][y] == 'S':
          start = (x, y, i)

  def bfs(start):
    x, y, z = start
    que = deque([(x, y, z, 0)])
    visited[z][x][y] = True

    while que:
      x, y, z, time = que.popleft()

      if board[z][x][y] == 'E':
        return time

      for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if 0 <= nx < R and 0 <= ny < C and 0 <= nz < L:
          if board[nz][nx][ny] != '#' and not visited[nz][nx][ny]:
            visited[nz][nx][ny] = True
            que.append((nx, ny, nz, time + 1))
            
    return -1

  result = bfs(start)
  
  if (result == -1):
    print("Trapped!")
  else:
    print(f"Escaped in {result} minute(s).")