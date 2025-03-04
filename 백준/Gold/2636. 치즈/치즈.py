import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())

# 치즈 개수 구하기
graph = []
cheeze = 0
for i in range(N):
  graph.append(list(map(int, input().split())))
  cheeze += sum(graph[i])


# 0인 구역 구하기
def bfs():
  que = deque([(0, 0)])
  melt = deque()
  
  while que:
    x, y = que.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
        visited[nx][ny] = True
        if graph[nx][ny] == 0:
          que.append((nx, ny))
        elif graph[nx][ny] == 1:
          melt.append((nx, ny))

  for x, y in melt:
    graph[x][y] = 0
  return len(melt)


melt_time = 1
while True:
  visited = [[False] * M for _ in range(N)]  
  melt_cnt = bfs()
  cheeze -= melt_cnt

  if cheeze == 0:
    print(melt_time)
    print(melt_cnt)
    break

  melt_time += 1