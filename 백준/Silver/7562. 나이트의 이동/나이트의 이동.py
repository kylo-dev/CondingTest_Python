from collections import deque

n = int(input())

dx = [2, 2, -2, -2, 1, -1, 1, -1]
dy = [1, -1, 1, -1, 2, 2, -2, -2]


def bfs(arr):
  while que:
    x, y = que.popleft()
    
    if x == mx and y == my:
      return arr[x][y]
    
    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < l and 0 <= ny < l:
        if arr[nx][ny] == 0:
          arr[nx][ny] = arr[x][y] + 1
          que.append((nx, ny))
        

for i in range(n):
  l = int(input())

  x, y = map(int, input().split())
  mx, my = map(int, input().split())

  arr = [[0] * l for _ in range(l)]
  arr[x][y] = 1
  
  que = deque([(x, y)])
  cnt = bfs(arr)
  print(cnt-1)
