import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

arr = [list(map(int, input().rstrip())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
  que = deque([(x, y)])

  while que :
    a, b = que.popleft()
  
    for i in range(4):
      nx = a + dx[i]
      ny = b + dy[i]
  
      if -1 < nx < n and -1 < ny < m and arr[nx][ny] == 1:
        arr[nx][ny] = arr[a][b] + 1
        que.append((nx, ny))
      

bfs(0, 0)
print(arr[-1][-1])