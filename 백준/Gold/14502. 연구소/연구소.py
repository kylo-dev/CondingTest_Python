import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
safe = []
virus = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 안전 영역 좌표
for i in range(N):
  for j in range(M):
    if arr[i][j] == 0:
      safe.append((i, j))
    elif arr[i][j] == 2:
      virus.append((i, j))

def bfs():
  que = deque(virus)
  infected = []

  while que:
    x, y = que.popleft()
    for k in range(4):
      nx = x + dx[k]
      ny = y + dy[k]
      if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0:
        arr[nx][ny] = 2
        infected.append((nx, ny))
        que.append((nx, ny))
  
  safe_count = sum(row.count(0) for row in arr)

  for x, y in infected:
    arr[x][y] = 0
  
  return safe_count


result = 0
for comb in combinations(safe, 3):
  for x, y in comb:
    arr[x][y] = 1
  
  result = max(result, bfs())
  
  for x, y in comb:
    arr[x][y] = 0

print(result)
