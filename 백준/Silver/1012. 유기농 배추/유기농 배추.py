import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**7)
t = int(input())

def dfs(x, y):
  if x<0 or x>=n or y<0 or y>=m:
    return False
  if graph[x][y] == 1:
    graph[x][y] = 0
    dfs(x-1, y)
    dfs(x, y-1)
    dfs(x+1, y)
    dfs(x, y+1)
    return True
    
  return False

for i in range(t):
  cnt = 0
  n, m, k = map(int, input().split())
  graph = [[0]*m for _ in range(n)]
  for j in range(k):
    t, v = map(int, input().split())
    graph[t][v] = 1

  for a in range(n):
    for b in range(m):
      if dfs(a, b) == True:
        cnt += 1
        
  print(cnt)