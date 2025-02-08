import sys
input = sys.stdin.readline
from collections import deque

N, M, K, X = map(int, input().split())
arr = [[] for _ in range(N + 1)]

for i in range(M):
  a, b = map(int, input().split())
  arr[a].append(b)

visited = [False for _ in range(N+1)]

def bfs(start):
  que = deque([(start, 0)])
  visited[start] = True
  ans = []

  while que:
    node, dist = que.popleft()

    if dist == K:
      ans.append(node)

    if dist < K:
      for next_node in arr[node]:
        if not visited[next_node]:
          que.append((next_node, dist + 1))
          visited[next_node] = True
  return ans

result = bfs(X)

if not result:
  print(-1)
else:
  for i in sorted(result):
    print(i)