import heapq, sys
input = sys.stdin.readline

N = int(input())
min_heap = []
answer = 0

for _ in range(N):
  heapq.heappush(min_heap, int(input()))

while len(min_heap) >= 2:
  a = heapq.heappop(min_heap)
  b = heapq.heappop(min_heap)
  answer += (a + b)

  heapq.heappush(min_heap, a + b)

print(answer)