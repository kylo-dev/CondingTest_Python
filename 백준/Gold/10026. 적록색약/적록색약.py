import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]


dx = [1,-1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, type):
  if type == 'G':
    graph[x][y] = 'r'
  else:
    graph[x][y] = type.lower()

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0<=nx<n and 0<=ny<n and graph[nx][ny]==type:
      dfs(nx, ny, type)

cnt = 0

for i in range(n):
  for j in range(n):
    if graph[i][j] == 'R':
      dfs(i, j, graph[i][j])
      cnt += 1
    elif graph[i][j] == 'G':
      dfs(i, j, graph[i][j])
      cnt += 1
    elif graph[i][j] == 'B':
      dfs(i, j, graph[i][j])
      cnt += 1

def dfs2(x, y , type):
  graph[x][y] = 0

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0<=nx<n and 0<=ny<n and graph[nx][ny]==type:
      dfs2(nx, ny, type)

cnt2 = 0

for i in range(n):
  for j in range(n):
    if graph[i][j] == 'r':
      dfs2(i, j ,'r')
      cnt2 += 1
    elif graph[i][j] == 'b':
      dfs2(i, j, 'b')
      cnt2 += 1

print(cnt, cnt2)