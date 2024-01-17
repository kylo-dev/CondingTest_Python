import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for i in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
  deq = deque([(x,y)])
  cnt = 1
  arr[x][y] = 0

  while deq:
    a, b = deq.popleft()
  
    for i in range(4):
      nx = a + dx[i]
      ny = b + dy[i]
  
      if -1 < nx < n and -1 < ny < m:
        if arr[nx][ny] != 0:
          arr[nx][ny] = 0
          cnt += 1
          deq.append((nx, ny))
  return cnt

num_list = []

for i in range(n):
  for j in range(m):
    if arr[i][j] == 1:
      cnt = bfs(i, j)
      num_list.append(cnt)

if len(num_list) == 0 :
  print(len(num_list))
  print(0)
else:
  print(len(num_list))
  print(max(num_list))