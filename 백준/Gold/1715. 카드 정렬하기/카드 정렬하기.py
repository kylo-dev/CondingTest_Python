import sys, heapq
input = sys.stdin.readline

N = int(input())
total = 0

que = []
for _ in range(N):
  heapq.heappush(que, int(input()))

if N == 1:
  print(0)
else:
  while len(que) > 1:
    first = heapq.heappop(que)
    second = heapq.heappop(que)
    total += (first + second)
    heapq.heappush(que, (first + second))
  
  print(total)