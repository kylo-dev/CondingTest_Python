import sys
import heapq
input = sys.stdin.readline

INF = 10 ** 9

V, E = map(int, input().split())
start = int(input())

graph = [[] for _ in range(V + 1)]
dist = [INF] * (V + 1)
dist[start] = 0

hq = [(0, start)]

for _ in range(E):
  u, v, w = map(int, input().split())
  graph[u].append((v, w))

while hq:
  d, x = heapq.heappop(hq)
  if d > dist[x]:
    continue

  for connected_x, weight in graph[x]:
    nd = d + weight
    if nd < dist[connected_x]:
      dist[connected_x] = nd
      heapq.heappush(hq, (nd, connected_x))

for i in range(1, V + 1):
  if dist[i] == INF:
    print("INF")
  else:
    print(dist[i])