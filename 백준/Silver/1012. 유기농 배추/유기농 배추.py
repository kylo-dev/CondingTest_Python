import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


for _ in range(T):
  M, N, K = map(int, input().split())
  graph = [[0] * N for _ in range(M)]
  count = 0

  for i in range(K):
    a, b = map(int, input().split())
    graph[a][b] = 1
  
  def dfs(x, y):
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] == 1:
        graph[nx][ny] = 0
        dfs(nx, ny)
  
  for i in range(M):
    for j in range(N):
      if graph[i][j] == 1:
        dfs(i, j)
        count += 1
  print(count)
  