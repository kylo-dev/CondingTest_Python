import sys
sys.setrecursionlimit(10**6)
from itertools import combinations

N, M = map(int, input().split())

graph = []
house = []
chicken = []
result = float("inf")

for i in range(N):
  graph.append(list(map(int, input().split())))
  for j in range(N):
    if graph[i][j] == 1:
      house.append((i, j))
    elif graph[i][j] == 2:
      chicken.append((i, j))

ans = []

def calculate_distance():
  global ans
  total = 0
  for hx, hy in house:
    ch_len = float("inf")
    for cx, cy in ans:
      ch_len = min(ch_len, abs(hx-cx) + abs(hy-cy))
    total += ch_len
  return total

def back(idx, cnt):
  global result

  if cnt == M:
    result = min(result, calculate_distance())
    return
  
  for i in range(idx, len(chicken)):
    ans.append(chicken[i])
    back(i + 1, cnt + 1)
    ans.pop()

back(0, 0)
print(result)
