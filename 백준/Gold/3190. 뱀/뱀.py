# 보드 크기
n = int(input())
data = [[0] * (n+1) for _ in range(n+1)]

# 사과 개수
k = int(input())
for _ in range(k):
  a, b = map(int, input().split())
  data[a][b] = 1

l = int(input())
info = []
for _ in range(l):
  x, c = input().split()
  info.append((int(x), c))

# 동남서북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
  if c == 'L':
    direction = (direction - 1) % 4
  else:
    direction = (direction + 1) % 4

  return direction

def simulate():
  x, y = 1, 1
  direction = 0
  index = 0
  time = 0
  q = [(x, y)]
  data[x][y] = 2
  
  while True:
    nx = x + dx[direction]
    ny = y + dy[direction]

    if 1 <= nx <= n and 1 <= ny <= n and data[nx][ny] != 2:
      if data[nx][ny] == 0:
        data[nx][ny] = 2
        qx, qy = q.pop(0)
        q.append((nx, ny))
        data[qx][qy] = 0
      elif data[nx][ny] == 1:
        data[nx][ny] = 2
        q.append((nx, ny))
    else:
      time += 1
      break

    x, y = nx, ny
    time += 1
    if index < l and info[index][0] == time:
      direction = turn(direction, info[index][1])
      index += 1
  return time

print(simulate())