from collections import deque
import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().split())

arr = [[] for _ in range(N + 1)]

for _ in range(M):
  a, b = map(int, input().split())
  arr[a].append(b)

visited = [False for _ in range(N+1)]

def bfs(start):
  que = deque([(start, 0)])
  visited[start] = True
  ans = []

  while que:
    node, count = que.popleft()

    if count == K:
      ans.append(node)
    
    if count < K:
        for n in arr[node]:
          if not visited[n]:
            que.append((n, count + 1))
            visited[n] = True
  
  return ans

result = bfs(X)

if result:
  result.sort()
  print(*result, sep="\n")
else:
  print(-1)
