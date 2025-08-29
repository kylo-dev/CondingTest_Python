import sys, heapq
input = sys.stdin.readline
INF = float('inf')

N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(E):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  graph[b].append((a, c))

v1, v2 = map(int, input().split())

def dijkstra(start):
  dist = [INF] * (N + 1)
  dist[start] = 0
  hq = [(0, start)]

  while hq:
    d, x = heapq.heappop(hq)

    if d > dist[x]:
      continue

    for connected_x, weight in graph[x]:
      dx = d + weight
      if dx < dist[connected_x]:
        dist[connected_x] = dx
        heapq.heappush(hq, (dx, connected_x))
  return dist

d1 = dijkstra(1)
d2 = dijkstra(v1)
d3 = dijkstra(v2)

case1 = d1[v1] + d2[v2] + d3[N]
case2 = d1[v2] + d3[v1] + d2[N]

answer = min(case1, case2)

if answer == INF:
  print(-1)
else:
  print(answer)
