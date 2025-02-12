import sys
sys.setrecursionlimit(10**6)
from itertools import combinations

N, M = map(int, input().split())

graph = []
house = []
chicken = []
ans = []
result = float("inf")

for i in range(N):
  graph.append(list(map(int, input().split())))
  for j in range(N):
    if graph[i][j] == 1:
      house.append((i, j))
    elif graph[i][j] == 2:
      chicken.append((i, j))


for comb in combinations(chicken, M):
  temp = 0

  for hx, hy in house:
    ch_len = float("inf")
    for cx, cy in comb:
      ch_len = min(ch_len, abs(hx - cx) + abs(hy - cy))
    temp += ch_len
  
  result = min(result, temp)

print(result)
