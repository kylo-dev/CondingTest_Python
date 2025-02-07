import sys, heapq
input = sys.stdin.readline

N = int(input())

que = []

for _ in range(N):
  num = int(input())
  if num == 0:
    if not que:
      print(0)
    else:
      print(heapq.heappop(que))
  else:
    heapq.heappush(que, num)