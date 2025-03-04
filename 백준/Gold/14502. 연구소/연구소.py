import sys
from collections import deque
from itertools import combinations
import copy
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

safe = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 안전 영역 좌표 구하기
for i in range(N):
  for j in range(M):
    if graph[i][j] == 0:
      safe.append((i, j))

# 바이러스 감염 bfs
def bfs(arr):
  que = deque()

  for i in range(N):
    for j in range(M):
      if arr[i][j] == 2:
        que.append((i, j))

  while que:
    x, y = que.popleft()
    for k in range(4):
      nx = x + dx[k]
      ny = y + dy[k]
      if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0:
        arr[nx][ny] = 2
        que.append((nx, ny))

# 벽을 세운 후 안전 영역 카운트
def safe_zone(arr):
  cnt = 0
  for i in arr:
    for j in i:
      if j == 0:
        cnt += 1
  return cnt

# 조합으로 3개의 벽 세우기
result = 0
for comb in combinations(safe, 3):
  arr = copy.deepcopy(graph)
  for x, y in comb:
    arr[x][y] = 1
  bfs(arr)
  result = max(result, safe_zone(arr))
    
# 값 출력
print(result)
