import sys
input = sys.stdin.readline

N = int(input())
K = int(input())

arr = [[0] * (N+1) for _ in range(N+1)]

for _ in range(K):
  x, y = map(int, input().split())
  arr[x][y] = 1

L = int(input())
moves = []
for _ in range(L):
  time, direct = input().split()
  moves.append((int(time), direct))

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
  arr[x][y] = 2

  direction = 0
  move_cnt = 0
  time = 0

  q = [(x, y)]

  while True:
    nx = x + dx[direction]
    ny = y + dy[direction]

    if 1 <= nx <= N and 1 <= ny <= N and arr[nx][ny] != 2:
      if arr[nx][ny] == 0:
        arr[nx][ny] = 2
        q.append((nx, ny))
        qx, qy = q.pop(0)
        arr[qx][qy] = 0
      elif arr[nx][ny] == 1:
        arr[nx][ny] = 2
        q.append((nx, ny))
    else:
      time += 1
      break
      
    x, y = nx, ny
    time += 1
    if move_cnt < L and time == moves[move_cnt][0]:
      direction = turn(direction, moves[move_cnt][1])
      move_cnt += 1
  return time

print(simulate())
