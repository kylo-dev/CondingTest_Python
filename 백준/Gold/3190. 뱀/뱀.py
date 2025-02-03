n = int(input())
k = int(input())
data = [[0] * (n+1) for _ in range(n+1)]
info = []

# 사과 정보
for _ in range(k):
  a, b = map(int, input().split())
  data[a][b] = 1

l = int(input())
for _ in range(l):
  x, c = input().split()
  info.append((int(x), c))

# 동남서북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
  if c == "L":
    direction = (direction - 1) % 4
  else:
    direction = (direction + 1) % 4
  return direction

def simulate():
  x, y = 1, 1
  data[x][y] = 2 # 뱀이 존재하는 위치 2로 표시

  direction = 0 # 0: 동쪽
  time = 0
  index = 0

  q = [(x, y)]
  while True:
    nx = x + dx[direction]
    ny = y + dy[direction]

    if 1 <= nx <= n and 1 <= ny <= n and data[nx][ny] != 2:
      if data[nx][ny] == 0:
        data[nx][ny] = 2
        q.append((nx, ny))
        qx, qy = q.pop(0)
        data[qx][qy] = 0
      elif data[nx][ny] == 1:
        data[nx][ny] = 2
        q.append((nx, ny))
    else:
      time += 1
      break

    x, y = nx, ny
    time += 1
    if index < l and time == info[index][0]:
      direction = turn(direction, info[index][1])
      index += 1
  return time

print(simulate())