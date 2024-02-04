n = int(input())

arr = [list(map(int, input())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y):
  global cnt
  arr[x][y] = 0
  cnt += 1
  
  for i in range(4):
    nx = x + dx[i]
    
    ny = y + dy[i]
    if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 1:
      dfs(nx, ny)
    
  return cnt

cnt_list = []

for i in range(n):
  for j in range(n):
    if arr[i][j] == 1:
      cnt = 0
      cnt_list.append(dfs(i, j))

print(len(cnt_list))
for i in sorted(cnt_list):
  print(i)