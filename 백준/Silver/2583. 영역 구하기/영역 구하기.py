import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

M, N, K = map(int, input().split())
graph = [[False] * M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = []

for _ in range(K):
  x1, y1, x2, y2 = map(int, input().split())
  for x in range(x1, x2):
    for y in range(y1, y2):
      graph[x][y] = True

def dfs(x, y):
  global cnt
  cnt += 1
  graph[x][y] = True
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < N and 0 <= ny < M and not graph[nx][ny]:
      dfs(nx, ny)
  return cnt

for i in range(N):
  for j in range(M):
    if not graph[i][j]:
      cnt = 0
      result.append(dfs(i, j))

result.sort()
print(len(result))
print(' '.join(map(str, result)))