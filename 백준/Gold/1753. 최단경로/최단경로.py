import sys
import heapq
input = sys.stdin.readline
INF = 10 ** 9

V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V + 1)]
dist = [INF] * (V + 1)
dist[K] = 0

for _ in range(E):
  u, v, w = map(int, input().split())
  graph[u].append((v, w))

hq = [(0, K)]

while hq:
  d, x = heapq.heappop(hq)

  if d > dist[x]:
    continue

  for connected_x, weight in graph[x]:
    dx = d + weight

    if dx < dist[connected_x]:
      dist[connected_x] = dx
      heapq.heappush(hq, (dx, connected_x))

for i in range(1, V + 1):
  if dist[i] == INF:
    print("INF")
  else:
    print(dist[i])