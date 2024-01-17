from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y):
  q = deque()
  dx = [1, -1, 0, 0]
  dy = [0, 0, 1, -1]
  q.append((x,y))
  arr[x][y] =0
  cnt = 1
  while q:
    a, b = q.popleft()
    for i in range(4):
      nx = a + dx[i]
      ny = b + dy[i]
      if -1<nx<n and -1<ny<m and arr[nx][ny] == 1:
        arr[nx][ny] = 0
        q.append((nx, ny))
        cnt += 1
  return cnt

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

num_list = []

for i in range(n):
  for j in range(m):
    if arr[i][j] == 1:
      cnt = bfs(i, j)
      num_list.append(cnt)

if len(num_list) == 0:
    print(len(num_list))
    print(0)
else:
    print(len(num_list))
    print(max(num_list))
        