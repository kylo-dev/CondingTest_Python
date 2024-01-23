import sys
input = sys.stdin.readline
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0 , 1, -1]

def fbfs():
  while fque:
    x, y = fque.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if not (-1 < nx < r and -1 < ny < c):
        continue  # 범위 밖은 패스
      if maze[nx][ny] == "#" or fire[nx][ny]:
        continue # "#" 이거나 1이면 이동할 수 없음
      fire[nx][ny] = fire[x][y] + 1
      fque.append((nx, ny))

def hbfs():
  while hque:
    x, y = hque.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if not (-1 < nx < r and -1 < ny < c):
        print(human[x][y])
        return
      if human[nx][ny] or maze[nx][ny] == "#":
        continue
      if fire[nx][ny] and human[x][y] + 1 >= fire[nx][ny]:
        continue
      human[nx][ny] = human[x][y] + 1
      hque.append((nx, ny))
      
  print("IMPOSSIBLE")
  return
  
      

r, c = map(int, input().split())

human = [[0] * c for _ in range(r)] # 사람 이동
fire = [[0] * c for _ in range(r)] # 불 이동
maze = [] # 미로
hque = deque()
fque = deque()


for i in range(r):
  maze.append(list(input().rstrip()))
  for j in range(c):
    if maze[i][j] == "J":
      hque.append((i, j))
      human[i][j] = 1
    elif maze[i][j] == "F":
      fque.append((i, j))
      fire[i][j] = 1

fbfs()
hbfs()