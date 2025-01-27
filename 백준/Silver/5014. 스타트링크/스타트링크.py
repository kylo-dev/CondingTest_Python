from collections import deque

f, s, g, u, d = map(int, input().split())
visited = [False] * (f + 1)
count = [0] * (f + 1)

def bfs(start):
  q = deque([start])
  visited[start] = True
  
  while q:
    current = q.popleft()

    if current == g:
      return count[g]

    for i in (current+u, current-d):
      if 0 < i <= f and not visited[i]:
        count[i] = count[current] + 1
        visited[i] = True
        q.append(i)
  
  return "use the stairs"
    
print(bfs(s))