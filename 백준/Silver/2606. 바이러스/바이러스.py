n = int(input())
k = int(input())
visited = [0 for i in range(n+1)]

graph = [[] for _ in range(n+1)]
for i in range(k):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
  
count = 0

def dfs(x):
  if visited[x] == 0:
    visited[x] = 1
    for i in graph[x]:
        dfs(i)
    
dfs(1)

print(sum(visited)-1)